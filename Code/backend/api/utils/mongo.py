from fastapi import HTTPException


async def get_or_404(record):
    """Gets the first record if exists or aborts the request"""
    if record.first():
        return record.first()
    else:
        raise HTTPException(404, 'Not Found')


async def get_all_or_404(records):
    """Gets all records if exists or aborts the request"""
    if records.first():
        return [record.to_mongo() for record in records]
    else:
        raise HTTPException(404, 'Not Found')
