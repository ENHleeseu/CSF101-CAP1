#This library allows you to programmatically control the mouse and keyboard to automate tasks on your computer.
import pyautogui
#It is used to introduce delays in the script.
import time
#This module is used to create and manage threads for concurrent execution.
import threading
#The queue module is used to create a task queue for managing the closing of tabs.
import queue

# Function to close a single tab
def close_tab():
    # Simulate the "Ctrl + W" keyboard 
    pyautogui.hotkey('ctrl', 'w')
    # Add a small delay to allow the tab to close
    time.sleep(1)
      
#worker function is to continuously check the task queue for tasks to be processed.
# Worker function to process tasks from the queue
def worker(q):
    #while loop that continues executing as long as the task queue q is not empty.
    while not q.empty():
        #checks if the queue is empty. If it's not empty, the loop continues.
        task = q.get()
        #    Inside the loop, this line retrieves the next task from the task queue q using the q.get() method.
        
        if task == "close_tab":
            #checks if the task obtained from the queue is equal to the string "close_tab".
            close_tab() 
            #used to keep track of the completion of tasks in the queue.
        q.task_done()

# Function to close multiple tabs using a queue
def close_tabs_with_queue(num_tabs_to_close):
    # Create a queue for tasks
    task_queue = queue.Queue()
    #    This line creates a new instance of a queue using the queue.Queue() class.
    #task_queue is now an empty queue that can be used to hold tasks.

    # Enqueue "close_tab" tasks for the specified number of tabs
    for _ in range(num_tabs_to_close):
        task_queue.put("close_tab")

    # Create a worker thread to process tasks
    worker_thread = threading.Thread(target=worker, args=(task_queue,))
    worker_thread.start()

    # Wait for the worker thread to finish
    worker_thread.join()
    #it checks whether the cript id being run as the ain program
if __name__ == "__main__":
    # Ensure that the Firefox is active 

    # Specify the number of tabs to close
    # Change this to the number of tabs you want to close
    num_tabs_to_close = 20
    # Close the specified number of tabs using a queue
    close_tabs_with_queue(num_tabs_to_close)
    