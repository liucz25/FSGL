TARGET = main
SRC = $(wildcard *.c)
OBJ = $(patsubst %.c ,%.o , $(SRC))
INCLUDE =     
DEFS = -DDEBUG              
CFLAGS = -g
CC = gcc
LIBS =    
RELEASE =release
SYMBOL=debug    

$(TARGET):$(OBJ)
	$(CC) $(DEFS) $(CFLAGS) $^ -o $@ $(INCLUDE) $(LIBS)
	
$(RELEASE):$(TARGET)
	objcopy --strip-debug $(TARGET) $(TSRGET).release
	strip $(TARGET).release
	
$(SYMBOL):$(TARGET)
	objcopy --only-keep-debug $(TARGET) $(TARGET).symbol

	
.PHONY:
clean:
	rm -rf *.o $(TARGET) $(TARGET).release
