



# name = Prompt.ask("[green]Enter Your Command Name[/green]")
# console.print(f"[yellow]{name}[/yellow] Not Found, Process Aborted",style="er")

sceam = {
    "name":"",
    "description":"",
    "status":"",
    "command":{
        "build":"",
        "run":"",
        "test":"",
        
    },
    "dependency":{
      "installer-command":""  ,
      "packages":[]
    },
    "todo":{
        "done":[],
        "left":[]
    }
}

def create_devg_file():
    name = Prompt.ask("[green]Enter Your Project Name[/green]")
    disc = Prompt.ask("[green]Description[/green]")
    buildC = Prompt.ask("[green]build command[/green]")
    runC = Prompt.ask("[green]run command[/green]")
    testC = Prompt.ask("[green]test command[/green]")
    console.print("Pkg Installer command should replace ",style="err")
    testC = Prompt.ask("[green]Pkg Installer Command[/green]")
    
    
    