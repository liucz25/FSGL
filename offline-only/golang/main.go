package main
 
import "fmt"


type Humanner interface{
	SayHi()
}
type  Student struct{
	name string
	id  int
}
func (tmp *Student) SayHi(){
	fmt.Println("fdsaas")
}


func main(){
	fmt.Println("hello world!!!")
//  var i Humanner

 s:=&Student{"meke",55}
//  i=s
 s.SayHi()


	}