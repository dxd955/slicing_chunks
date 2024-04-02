import pandas as pd
from slicing_chunks import slicing_chunk


DFS = pd.date_range("2023-01-01 00:00:00", "2023-01-01 00:00:05", freq="s")
DF = pd.DataFrame({"dt": DFS.repeat(3)})



def test_chunker_sizes(): #Тест на корректность размера чанков
    for chunk in slicing_chunk(DF, 2):
        assert len(chunk) >= 2, "incorrect"
        print("correct")


def test_chunker_dt_intersec(): #Тест на отсутствие пересечения дат между чанками
    prev_end_date = None
    for chunk in slicing_chunk(DF, 2):
        if prev_end_date:
            assert prev_end_date != chunk.iloc[0]['dt']
        prev_end_date = chunk.iloc[-1]['dt']

def test_chunker_edge_cases(): #Тест на обработку крайних случаев
    assert len(list(slicing_chunk(DF, len(DF)))) == 1
