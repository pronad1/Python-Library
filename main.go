package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

func runCmd(name string, arg ...string) {
	cmd := exec.Command(name, arg...)
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func clearTerminal() {
	switch runtime.GOOS {
	case "darwin":
		runCmd("clear")
	case "linux":
		runCmd("clear")
	case "windows":
		runCmd("cmd", "/c", "cls")
	default:
		runCmd("clear")
	}
}

type Todo struct {
	Description string
	Status      bool
}

var todos []Todo

func main() {
	clearTerminal()
	printWelcomeBanner()
	printCommands()

	for {
		var command string
		fmt.Print("Enter command:\n\t> ")
		reader := bufio.NewReader(os.Stdin)
		input, err := reader.ReadString('\n')

		if err != nil {
			fmt.Println("Error reading command")
			break
		}

		command = strings.TrimSpace(input)
		parts := strings.Fields(command)

		if len(parts) == 0 {
			continue
		}

		switch parts[0] {
		case "tasks":
			printTodos()
		case "commands":
			printCommands()
		case "quit":
			return
		case "add":
			if len(parts) > 1 {

				taskDescription := strings.Join(parts[1:], " ")
				addTodo(taskDescription)
			} else {
				fmt.Println("Usage: add <task description>")
			}
		case "done":
			if len(parts) > 1 {
				indexStr := parts[1]
				index, err := strconv.Atoi(indexStr)
				if err != nil {
					fmt.Println("Invalid index. Please enter a number.")
				} else {
					markTodoDone(index)
				}
			} else {
				fmt.Println("Usage: done <index>")
			}
		case "clear":
			clearTerminal()
		default:
			fmt.Println("Command not found")
			printCommands()
		}

	}
}

func printCommands() {
	fmt.Println("")
	fmt.Println("Available commands:")
	fmt.Println("\t> add <task>: Add a new task")
	fmt.Println("\t> tasks: View to-do list")
	fmt.Println("\t> done <index>: Mark task as done by its index")
	fmt.Println("\t> commands: View available commands")
	fmt.Println("\t> clear: Clear the terminal")
	fmt.Println("\t> quit: Quit app")
	fmt.Println("")
}

func printWelcomeBanner() {
	fmt.Println("********************************************")
	fmt.Println("||                                        ||")
	fmt.Println("||          Welcome to Carpe Diem         ||")
	fmt.Println("||        Your Task Management CLI App    ||")
	fmt.Println("||                                        ||")
	fmt.Println("********************************************")
	fmt.Println("")
}


func addTodo(description string) {
	todos = append(todos, Todo{Description: description, Status: false})
	fmt.Printf("\nTask '%s' added successfully!\n\n", description)
}


func markTodoDone(index int) {
	if index > 0 && index <= len(todos) {
		todos[index-1].Status = true
		fmt.Printf("\nTask '%s' marked as done.\n\n", todos[index-1].Description)
	} else {
		fmt.Println("Invalid task index.\n")
	}
}

func printTodos() {
	if len(todos) == 0 {
		fmt.Println("\nNo tasks yet.\n")
		return
	}

	fmt.Println("\nCurrent Tasks")

	for i := 0; i < len(todos); i++ {
		status := "[ ]"
		if todos[i].Status {
			status = "[x]"
		}

		fmt.Printf("\t%d: %s %s \n", i+1, status, todos[i].Description)
	}
	fmt.Println("")
}package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

func runCmd(name string, arg ...string) {
	cmd := exec.Command(name, arg...)
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func clearTerminal() {
	switch runtime.GOOS {
	case "darwin":
		runCmd("clear")
	case "linux":
		runCmd("clear")
	case "windows":
		runCmd("cmd", "/c", "cls")
	default:
		runCmd("clear")
	}
}

type Todo struct {
	Description string
	Status      bool
}

var todos []Todo

func main() {
	clearTerminal()
	printWelcomeBanner()
	printCommands()

	for {
		var command string
		fmt.Print("Enter command:\n\t> ")
		reader := bufio.NewReader(os.Stdin)
		input, err := reader.ReadString('\n')

		if err != nil {
			fmt.Println("Error reading command")
			break
		}

		command = strings.TrimSpace(input)
		parts := strings.Fields(command)

		if len(parts) == 0 {
			continue
		}

		switch parts[0] {
		case "tasks":
			printTodos()
		case "commands":
			printCommands()
		case "quit":
			return
		case "add":
			if len(parts) > 1 {

				taskDescription := strings.Join(parts[1:], " ")
				addTodo(taskDescription)
			} else {
				fmt.Println("Usage: add <task description>")
			}
		case "done":
			if len(parts) > 1 {
				indexStr := parts[1]
				index, err := strconv.Atoi(indexStr)
				if err != nil {
					fmt.Println("Invalid index. Please enter a number.")
				} else {
					markTodoDone(index)
				}
			} else {
				fmt.Println("Usage: done <index>")
			}
		case "clear":
			clearTerminal()
		default:
			fmt.Println("Command not found")
			printCommands()
		}

	}
}

func printCommands() {
	fmt.Println("")
	fmt.Println("Available commands:")
	fmt.Println("\t> add <task>: Add a new task")
	fmt.Println("\t> tasks: View to-do list")
	fmt.Println("\t> done <index>: Mark task as done by its index")
	fmt.Println("\t> commands: View available commands")
	fmt.Println("\t> clear: Clear the terminal")
	fmt.Println("\t> quit: Quit app")
	fmt.Println("")
}

func printWelcomeBanner() {
	fmt.Println("********************************************")
	fmt.Println("||                                        ||")
	fmt.Println("||          Welcome to Carpe Diem         ||")
	fmt.Println("||        Your Task Management CLI App    ||")
	fmt.Println("||                                        ||")
	fmt.Println("********************************************")
	fmt.Println("")
}


func addTodo(description string) {
	todos = append(todos, Todo{Description: description, Status: false})
	fmt.Printf("\nTask '%s' added successfully!\n\n", description)
}


func markTodoDone(index int) {
	if index > 0 && index <= len(todos) {
		todos[index-1].Status = true
		fmt.Printf("\nTask '%s' marked as done.\n\n", todos[index-1].Description)
	} else {
		fmt.Println("Invalid task index.\n")
	}
}

func printTodos() {
	if len(todos) == 0 {
		fmt.Println("\nNo tasks yet.\n")
		return
	}

	fmt.Println("\nCurrent Tasks")

	for i := 0; i < len(todos); i++ {
		status := "[ ]"
		if todos[i].Status {
			status = "[x]"
		}

		fmt.Printf("\t%d: %s %s \n", i+1, status, todos[i].Description)
	}
	fmt.Println("")
}package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

func runCmd(name string, arg ...string) {
	cmd := exec.Command(name, arg...)
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func clearTerminal() {
	switch runtime.GOOS {
	case "darwin":
		runCmd("clear")
	case "linux":
		runCmd("clear")
	case "windows":
		runCmd("cmd", "/c", "cls")
	default:
		runCmd("clear")
	}
}

type Todo struct {
	Description string
	Status      bool
}

var todos []Todo

func main() {
	clearTerminal()
	printWelcomeBanner()
	printCommands()

	for {
		var command string
		fmt.Print("Enter command:\n\t> ")
		reader := bufio.NewReader(os.Stdin)
		input, err := reader.ReadString('\n')

		if err != nil {
			fmt.Println("Error reading command")
			break
		}

		command = strings.TrimSpace(input)
		parts := strings.Fields(command)

		if len(parts) == 0 {
			continue
		}

		switch parts[0] {
		case "tasks":
			printTodos()
		case "commands":
			printCommands()
		case "quit":
			return
		case "add":
			if len(parts) > 1 {

				taskDescription := strings.Join(parts[1:], " ")
				addTodo(taskDescription)
			} else {
				fmt.Println("Usage: add <task description>")
			}
		case "done":
			if len(parts) > 1 {
				indexStr := parts[1]
				index, err := strconv.Atoi(indexStr)
				if err != nil {
					fmt.Println("Invalid index. Please enter a number.")
				} else {
					markTodoDone(index)
				}
			} else {
				fmt.Println("Usage: done <index>")
			}
		case "clear":
			clearTerminal()
		default:
			fmt.Println("Command not found")
			printCommands()
		}

	}
}

func printCommands() {
	fmt.Println("")
	fmt.Println("Available commands:")
	fmt.Println("\t> add <task>: Add a new task")
	fmt.Println("\t> tasks: View to-do list")
	fmt.Println("\t> done <index>: Mark task as done by its index")
	fmt.Println("\t> commands: View available commands")
	fmt.Println("\t> clear: Clear the terminal")
	fmt.Println("\t> quit: Quit app")
	fmt.Println("")
}

func printWelcomeBanner() {
	fmt.Println("********************************************")
	fmt.Println("||                                        ||")
	fmt.Println("||          Welcome to Carpe Diem         ||")
	fmt.Println("||        Your Task Management CLI App    ||")
	fmt.Println("||                                        ||")
	fmt.Println("********************************************")
	fmt.Println("")
}


func addTodo(description string) {
	todos = append(todos, Todo{Description: description, Status: false})
	fmt.Printf("\nTask '%s' added successfully!\n\n", description)
}


func markTodoDone(index int) {
	if index > 0 && index <= len(todos) {
		todos[index-1].Status = true
		fmt.Printf("\nTask '%s' marked as done.\n\n", todos[index-1].Description)
	} else {
		fmt.Println("Invalid task index.\n")
	}
}

func printTodos() {
	if len(todos) == 0 {
		fmt.Println("\nNo tasks yet.\n")
		return
	}

	fmt.Println("\nCurrent Tasks")

	for i := 0; i < len(todos); i++ {
		status := "[ ]"
		if todos[i].Status {
			status = "[x]"
		}

		fmt.Printf("\t%d: %s %s \n", i+1, status, todos[i].Description)
	}
	fmt.Println("")
}package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

func runCmd(name string, arg ...string) {
	cmd := exec.Command(name, arg...)
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func clearTerminal() {
	switch runtime.GOOS {
	case "darwin":
		runCmd("clear")
	case "linux":
		runCmd("clear")
	case "windows":
		runCmd("cmd", "/c", "cls")
	default:
		runCmd("clear")
	}
}

type Todo struct {
	Description string
	Status      bool
}

var todos []Todo

func main() {
	clearTerminal()
	printWelcomeBanner()
	printCommands()

	for {
		var command string
		fmt.Print("Enter command:\n\t> ")
		reader := bufio.NewReader(os.Stdin)
		input, err := reader.ReadString('\n')

		if err != nil {
			fmt.Println("Error reading command")
			break
		}

		command = strings.TrimSpace(input)
		parts := strings.Fields(command)

		if len(parts) == 0 {
			continue
		}

		switch parts[0] {
		case "tasks":
			printTodos()
		case "commands":
			printCommands()
		case "quit":
			return
		case "add":
			if len(parts) > 1 {

				taskDescription := strings.Join(parts[1:], " ")
				addTodo(taskDescription)
			} else {
				fmt.Println("Usage: add <task description>")
			}
		case "done":
			if len(parts) > 1 {
				indexStr := parts[1]
				index, err := strconv.Atoi(indexStr)
				if err != nil {
					fmt.Println("Invalid index. Please enter a number.")
				} else {
					markTodoDone(index)
				}
			} else {
				fmt.Println("Usage: done <index>")
			}
		case "clear":
			clearTerminal()
		default:
			fmt.Println("Command not found")
			printCommands()
		}

	}
}

func printCommands() {
	fmt.Println("")
	fmt.Println("Available commands:")
	fmt.Println("\t> add <task>: Add a new task")
	fmt.Println("\t> tasks: View to-do list")
	fmt.Println("\t> done <index>: Mark task as done by its index")
	fmt.Println("\t> commands: View available commands")
	fmt.Println("\t> clear: Clear the terminal")
	fmt.Println("\t> quit: Quit app")
	fmt.Println("")
}

func printWelcomeBanner() {
	fmt.Println("********************************************")
	fmt.Println("||                                        ||")
	fmt.Println("||          Welcome to Carpe Diem         ||")
	fmt.Println("||        Your Task Management CLI App    ||")
	fmt.Println("||                                        ||")
	fmt.Println("********************************************")
	fmt.Println("")
}


func addTodo(description string) {
	todos = append(todos, Todo{Description: description, Status: false})
	fmt.Printf("\nTask '%s' added successfully!\n\n", description)
}


func markTodoDone(index int) {
	if index > 0 && index <= len(todos) {
		todos[index-1].Status = true
		fmt.Printf("\nTask '%s' marked as done.\n\n", todos[index-1].Description)
	} else {
		fmt.Println("Invalid task index.\n")
	}
}

func printTodos() {
	if len(todos) == 0 {
		fmt.Println("\nNo tasks yet.\n")
		return
	}

	fmt.Println("\nCurrent Tasks")

	for i := 0; i < len(todos); i++ {
		status := "[ ]"
		if todos[i].Status {
			status = "[x]"
		}

		fmt.Printf("\t%d: %s %s \n", i+1, status, todos[i].Description)
	}
	fmt.Println("")
}package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

func runCmd(name string, arg ...string) {
	cmd := exec.Command(name, arg...)
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func clearTerminal() {
	switch runtime.GOOS {
	case "darwin":
		runCmd("clear")
	case "linux":
		runCmd("clear")
	case "windows":
		runCmd("cmd", "/c", "cls")
	default:
		runCmd("clear")
	}
}

type Todo struct {
	Description string
	Status      bool
}

var todos []Todo

func main() {
	clearTerminal()
	printWelcomeBanner()
	printCommands()

	for {
		var command string
		fmt.Print("Enter command:\n\t> ")
		reader := bufio.NewReader(os.Stdin)
		input, err := reader.ReadString('\n')

		if err != nil {
			fmt.Println("Error reading command")
			break
		}

		command = strings.TrimSpace(input)
		parts := strings.Fields(command)

		if len(parts) == 0 {
			continue
		}

		switch parts[0] {
		case "tasks":
			printTodos()
		case "commands":
			printCommands()
		case "quit":
			return
		case "add":
			if len(parts) > 1 {

				taskDescription := strings.Join(parts[1:], " ")
				addTodo(taskDescription)
			} else {
				fmt.Println("Usage: add <task description>")
			}
		case "done":
			if len(parts) > 1 {
				indexStr := parts[1]
				index, err := strconv.Atoi(indexStr)
				if err != nil {
					fmt.Println("Invalid index. Please enter a number.")
				} else {
					markTodoDone(index)
				}
			} else {
				fmt.Println("Usage: done <index>")
			}
		case "clear":
			clearTerminal()
		default:
			fmt.Println("Command not found")
			printCommands()
		}

	}
}

func printCommands() {
	fmt.Println("")
	fmt.Println("Available commands:")
	fmt.Println("\t> add <task>: Add a new task")
	fmt.Println("\t> tasks: View to-do list")
	fmt.Println("\t> done <index>: Mark task as done by its index")
	fmt.Println("\t> commands: View available commands")
	fmt.Println("\t> clear: Clear the terminal")
	fmt.Println("\t> quit: Quit app")
	fmt.Println("")
}

func printWelcomeBanner() {
	fmt.Println("********************************************")
	fmt.Println("||                                        ||")
	fmt.Println("||          Welcome to Carpe Diem         ||")
	fmt.Println("||        Your Task Management CLI App    ||")
	fmt.Println("||                                        ||")
	fmt.Println("********************************************")
	fmt.Println("")
}


func addTodo(description string) {
	todos = append(todos, Todo{Description: description, Status: false})
	fmt.Printf("\nTask '%s' added successfully!\n\n", description)
}


func markTodoDone(index int) {
	if index > 0 && index <= len(todos) {
		todos[index-1].Status = true
		fmt.Printf("\nTask '%s' marked as done.\n\n", todos[index-1].Description)
	} else {
		fmt.Println("Invalid task index.\n")
	}
}

func printTodos() {
	if len(todos) == 0 {
		fmt.Println("\nNo tasks yet.\n")
		return
	}

	fmt.Println("\nCurrent Tasks")

	for i := 0; i < len(todos); i++ {
		status := "[ ]"
		if todos[i].Status {
			status = "[x]"
		}

		fmt.Printf("\t%d: %s %s \n", i+1, status, todos[i].Description)
	}
	fmt.Println("")
}