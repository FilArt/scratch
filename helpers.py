def split_by_chunks(data: list, chunk_size: int):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]
