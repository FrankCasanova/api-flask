from zipfile import ZipFile

async def zipped(file):
    zip_object = ZipFile(file)