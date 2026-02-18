import tqdm
from tqdm import tqdm
import time

# Function creation for the loading bar
def loading_bar(iterations=100, delay=0.1, description="Loading", milestones=None, hold_time=3):
    # Sets milestones to none and keeps defined description if no Milestones defined
    if milestones is None:
        milestones = {}
    with tqdm(
        total = iterations,
        #This is the initial desctiption
        desc = description,
        # Formatting of the loading bar
        bar_format = "{desc:<15}: {percentage:.0f}%|{bar:50}|",
        # Removes loading bar once it has reached 100%
        leave = False,
        colour="blue"
    ) as pbar:
        for i in range(50):
            if i in milestones:
                pbar.set_description(milestones[i])
            # Controlls how fast/slow the loading bar is
            time.sleep(delay)
            pbar.update(1)

# Block to determine when to progress the bar based on switch output

        # while True:
        #     if chan.recv():
        #         buffer += chan.recv(4096).decode(errors="ignore")
        #         if ssh_milestone_text in buffer:
        #             break
        #     time.sleep(0.1)

        # Simulates break to test loading before/after
        # time.sleep(5)
        
        for i in range(50, 100):
            if i in milestones:
                pbar.set_description(milestones[i])
            # Controlls how fast/slow the loading bar is
            time.sleep(delay)
            pbar.update(1)
        # Sets description after the bar is full
        pbar.set_description("Complete")
        time.sleep(hold_time)
        pbar.clear()

# Can be used to define description changes upon reaching specific milestones in the loading
# Based on Iterations being set to 100. Requires adjustment if you change the iterations count
milestones_markers = {
    0: "Starting",
    25: "Quarter", 
    50: "Half",
    75: "Almost Done"
    }

# Calls function with defined milestone markers. Can be called without any variables for basic loading bar.
loading_bar(milestones=milestones_markers)

