import azure.functions as func
import datetime
import json
import logging
import random

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False) 
def TimerTriggerFunction(myTimer: func.TimerRequest) -> None:
	current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	random_log = "OK" if random.random() > 0.1 else "ERROR"
	logging.info(f"Ran at {current_time} {'(past due)' if myTimer.past_due else ''} with: {random_log}")

