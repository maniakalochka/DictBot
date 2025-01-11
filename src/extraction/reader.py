import csv
import random
import aiofiles


filename = "./datasets/oxford5000.csv"


async def reader(filename) -> dict:
    async with aiofiles.open(filename, mode="r", encoding="utf-8") as file:
        content = await file.read()
        reader = csv.DictReader(content.splitlines())
        random_word = random.choice(list(reader))
        return random_word
