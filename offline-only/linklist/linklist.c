#include "linklist.h"
db_list_pt core_list_create(void)
{
    db_list_pt list_head = NULL;
    list_head = (db_list_pt)malloc(sizeof(db_list_t));
    if (list_head == NULL)
    {
        errno = ENOMEM;
        exit(errno);
    }
    list_head->limit_size = 0;
    list_head->head = (db_node_pt)malloc(sizeof(db_node_t));
    if (list_head == NULL)
    {
        errno = ENOMEM;
        exit(errno);
    }
    list_head->head->next = list_head->head->prev = NULL;
    list_head->head->data = NULL;
    list_head->tail = list_head->head;
    return list_head;
}

int core_list_insert_before(db_list_t **list_head, int num, void *new_node_data)
{

    u32 counter = 1;
    db_node_pt current = NULL;
    db_node_pt new_node = NULL;

    if (list_head == NULL || *list_head == NULL)
    {
        errno = EINVAL;
        exit(errno);
    }
    if ((*list_head)->limit_size != 0)
    {
        new_node = (db_node_pt)malloc(sizeof(db_node_t));
        if (new_node == NULL)
        {
            errno = ENOMEM;
            exit(errno);
        }
        new_node->data = new_node_data;
        new_node->prev = new_node->next = NULL;
        if (num > 0 && num <= (*list_head)->limit_size)
        {
            current = (*list_head)->head;
            while (counter < num)
            {
                counter++;
                current = current->next;
            }
            if (counter == 1)
            {
                (*list_head)->head->prev = new_node;
                new_node->next = (*list_head)->head;
                (*list_head)->head = new_node;
                (*list_head)->limit_size++;
                return 0;
            }
            current->prev->next = new_node;
            new_node->prev = current->prev;
            current->prev = new_node;
            new_node->next = current;
            (*list_head)->limit_size++;
            return 0;
        }
    }
/*    else
    {
        errno = EINVAL;
        free(new_node);
        new_node = NULL;
        return -1;
    }
*/
    if (num != 0)
    {
        errno = EINVAL;
        exit(errno);
    }
    (*list_head)->head->data = new_node_data;
    (*list_head)->limit_size++;
    return 0;
}

int core_list_insert_after(db_list_t **list_head, int num, void *new_node_data)
{

    u32 counter = 1;
    db_node_pt current = NULL;
    db_node_pt new_node = NULL;

    if (list_head == NULL || *list_head == NULL)
    {
        errno = EINVAL;
        exit(errno);
    }
    if ((*list_head)->limit_size != 0)
    {
        new_node = (db_node_pt)malloc(sizeof(db_node_t));
        if (new_node == NULL)
        {
            errno = ENOMEM;
            exit(errno);
        }
        new_node->data = new_node_data;
        new_node->prev = new_node->next = NULL;
        if (num > 0 && num <= (*list_head)->limit_size)
        {
            current = (*list_head)->head;
            while (counter < num)
            {
                counter++;
                current = current->next;
                if (current->next == NULL)
                {
                    (*list_head)->tail = new_node;
                    current->next = new_node;
                    new_node->prev = current;
                    (*list_head)->limit_size++;
                    return 0;
                }
                new_node->prev = current;
                new_node->next = current->next;
                current->next = new_node;
                current->next->prev = new_node;
                (*list_head)->limit_size++;
                return 0;
            }
        }
        else
        {
            if (num != 0)
            {
                errno = EINVAL;
                exit(errno);
            }
            (*list_head)->head->data = new_node_data;
            (*list_head)->limit_size++;
            return 0;
        }
    }
}

int core_list_delete(db_list_t **list_head, int num)
{
    int counter = 1;
    db_node_pt current = NULL;
    db_node_pt tmp = NULL;
    if (list_head == NULL || *list_head == NULL)
    {
        errno = EINVAL;
        exit(errno);
    }
    current = (*list_head)->head;
    while (counter < num)
    {
        counter++;
        current = current->next;
    }
    if (counter == 1)
    {
        tmp = (*list_head)->head;
        (*list_head)->head->prev = NULL;
        (*list_head)->head = (*list_head)->head->next;
        free(tmp);
        tmp = NULL;
        (*list_head)->limit_size--;
        return 0;
    }
    if ((*list_head)->limit_size == counter)
    {
        tmp = (*list_head)->tail;
        (*list_head)->tail = (*list_head)->tail->prev;
        free(tmp);
        tmp = NULL;
        (*list_head)->tail->next = NULL;
        (*list_head)->limit_size--;
        return 0;
    }
    tmp = current;
    current->prev->next = current->next;
    current->next->prev = current->prev;
    free(tmp);
    tmp = NULL;
    (*list_head)->limit_size--;
    return 0;
}

int core_list_modify(db_list_t **list_head, int num, void *new_node_data)
{
    u32 counter = 0;
    db_node_pt current = NULL;

    if (list_head == NULL || *list_head == NULL || num < 0 || num > (*list_head)->limit_size)
    {
        errno = EINVAL;
        exit(errno);
    }
    current - (*list_head)->head;
    while (counter != num - 1)
    {
        counter++;
        current = current->next;
    }
    current->data = new_node_data;
    return 0;
}

/*void core_list_show(db_list_t **list_head)
{


}*/
//遍历
static inline void *__core_list_visit(db_list_t **list_head, u32 num)
{
    int counter = 0;
    if (list_head == NULL || (*list_head) == NULL || num < 0 || num > (*list_head)->limit_size)
    {
        errno = EINVAL;
        exit(errno);
    }
    db_node_pt current = (*list_head)->head;
    for (counter = 0; counter < num; counter++)
    {
        current = current->next;
    }
    return (void *)(current->data);
}

void core_list_cuid(db_list_t *list_head, void (*do_function)(void *))
{
    u32 i = 0;
    if (list_head == NULL || list_head->limit_size < 0)
    {
        errno = EINVAL;
        exit(errno);
    }
    for (i = 0; i < list_head->limit_size; i++)
    {
        (* do_function)(__core_list_visit(&list_head, i));
    }
}
int core_listLsearch(db_list_t **list_head, void *find_data, int (*compare)(void *, void *))
{
    int counter = 1;
    db_node_pt current = (*list_head)->head;
    if (list_head == NULL || *list_head == NULL)
    {
        errno = EINVAL;
        exit(errno);
    }
    current = (*list_head)->head;
    while (compare(current->data, find_data) != 0 && current->next != NULL)
    {
        current = current->next;
        counter++;
    }
    if (current->next == NULL && compare(current->data, find_data) != 0)
        return 0;
    return counter;
}
