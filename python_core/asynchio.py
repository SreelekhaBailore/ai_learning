import asyncio

async def processTask(taskId):
    print(f"Processing task {taskId}...")
    await asyncio.sleep(2)  # Simulate a time-consuming task
    print(f"Task {taskId} completed.")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(processTask(1))
        tg.create_task(processTask(2))
    


asyncio.run(main())
    
    

