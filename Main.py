from datetime import datetime
Todolist=[]
class newTask:
    def __init__(self,Day,Time) :
         count=0
         self._Day=Day
         self._Time=Time
         self._Completion_status=0
    def set_Task(self,String):
        self._String=String
    #here i define a function to view the todo list
def View_ToDo_List():
    Task_specified=int(input("do you want to specify a task?"))
    if Task_specified==1:
        i=int(input("enter the task here:"))
        task=Todolist[i]
        print("Day:",task._Day,"Time:",task._Time,"completion_status:",task._Completion_status,"Task:",task._String)
    elif Task_specified==0:
      for i in range(len(Todolist)):
           task=Todolist[i]
           print("Day:",task._Day,"Time:",task._Time,"completion_status:",task._Completion_status,"Task:",task._String)
    #with this function i can add new elements to my todo list
def Add_New_Task():
    Day=datetime.now()
    Time=datetime.now()
    Day=Day.strftime("%A")
    Time=Time.strftime("%H,%M,%S")
    task=newTask(Day=Day,Time=Time)
    for i in range(1):
        #Enter_new_task=int(input("Enter new task?"))
        #if Enter_new_task==0:
         #   break
        #elif Enter_new_task==1:
            task.set_Task(input('enter a new task:')) 
            if task in Todolist:
                break
            else:
                 Todolist.append(task)
              
def Mark_Task_Completed():
    for i in range(len(Todolist)-1):
        task=Todolist[i]
        completion_status=int(input("is task completed?"))
        if completion_status==0:
            task._completion_status=0
        elif completion_status==1:
            task._completion_status=1
            Remove_Task(task)
def Remove_Task(task):
    if task._completion_status==1:
        Todolist.remove(task)
    
def Exit_program():
    return -1
        
        
displaycases = {
        1: View_ToDo_List,
        2: Add_New_Task,
        3: Mark_Task_Completed,
        4: Remove_Task,
        5: Exit_program
      }
def main():
   while True:
        input_case=int(input("enter a number:"))
        if input_case in displaycases:
              displaycases[input_case]()
        else:
           print("invalide input.please enter correct input")
        if input_case ==5:
            break

main()
    