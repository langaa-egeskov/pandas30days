import pandas as pd
import numpy as np


World = pd.DataFrame(
    [], columns=["name", "continent", "area", "population", "gdp"]
).astype(
    {
        "name": "object",
        "continent": "object",
        "area": "Int64",
        "population": "Int64",
        "gdp": "Int64",
    }
)


World.loc[len(World.index)] = ["Afghanistan", "Asia", 652230, 25500100, np.int64(2.0343e10)]
World.loc[len(World.index)] = ["Albania", "Europe", 28748, 2831741, 1.296e10]
World.loc[len(World.index)] = ["Algeria", "Africa", 2381741, 37100000, 1.88681e11]
World.loc[len(World.index)] = ["Andorra","Europe", 468, 78115, 3.712e9]
World.loc[len(World.index)] = ["Angola", "Africa", 1246700, 20609294, 1.0099e11]

print("World")
print(World)
print()

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3e6) | (world['population'] > 25e6)]
    return df[['name', 'population', 'area']]

print("Big Countries")
print(big_countries(World))