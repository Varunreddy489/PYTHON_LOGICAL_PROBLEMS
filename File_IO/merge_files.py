import time
import asyncio
import aiofiles

def file_reader(input_file):
    with open(input_file, "r") as file:
        for line in file:
            yield line  

def merge_files(output_file, *input_files):
    with open(output_file, "w") as w:
        for input_file in input_files:
            for line in file_reader(input_file):  
                w.write(line)

start = time.time()
merge_files('output.txt', '90M.txt', '98M.txt', '99M.txt', '95M.txt')
print(f"Time taken: {time.time() - start:.2f} seconds")




async def read_file(filename):
    async with aiofiles.open(filename) as file:
        return await file.read()


async def write_files_to_output(input_file,output_file):

    tasks = [read_file(file) for file in input_file]


    contents = await asyncio.gather(*tasks)


    async with aiofiles.open(output_file,"w") as file:
        for content in contents:
            await file.write(content + "\n")


input_files = ['90M.txt', '98M.txt', '99M.txt', '95M.txt']

output_file = "combined.txt"

start=time.time()
asyncio.run(write_files_to_output(input_files,output_file))
print(time.time()-start )