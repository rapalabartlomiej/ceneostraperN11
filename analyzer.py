import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as pit

print(*[filename.removesuffix(".json") for filename in os.listdir("./opinions")],sep="\n")
product_code = input("podaj kod prodduktu: ")

opinions = pd.read_json(f"opinions/{product_code}.json")


opinions.score = opinions.score.map(lambda x: x.split("/")[0].replace(",",".")).astype(float)


stats = {
    "opinion_count":opinions.shape[0],
    "pros_count":opinions.pros.astype(bool).sum(),
    "cons_count":opinions.cons.astype(bool).sum(),
    "average_score":opinions.score.mean,
}
print(f"""Dla produktu o kodzie {product_code}
pobrancyh zostalo {stats["opinion_count"]} opini
Dla {stats["pros_count"]} opini podana zostala lista zalet produktu
a dla {stats["cons_count"]} opini podana zaostala lista wad.
Srednia ocena produktu wynosi {stats["average_score"]}""")
print("---------------")
print(opinions)

stars = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
stars.plot.bar()
pit.show()

recommendation_counts = opinions.recommendation.value_counts(dropna=False)
recommendation_counts.plot.pie(autopct='%1.1f%%', startangle=90)
pit.axis('equal')
pit.legend(title="Rekomendacja")
pit.show()
