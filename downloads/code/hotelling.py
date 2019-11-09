%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Firm:
    def __init__(init_state, name):
        self.init_state = init_state
        self.name = name
        self.step = 1
        self.current_state = init_state
        sefl.next_state = 0


class FirmColletion:
    def __init__(*firms):
        self.firms = firms
        self.dist_euclidean = np.vectorize(_dist_euclidean, signature='(n),(n)->()')

    def rank(self):
        return np.argsort(self.get('current_state'))

    def get(self, attr):
        return [getattr(self, attr) for firm in self.firms]

    @staticmethod
    def dist_euclidean(a):
        res = np.empty((len(a), len(a)))
        for i, ai in enumerate(a):
            res[i, :] = np.subtract(a, ai)
        return res

    def distance(self):
        positions = np.array(self.get('current_state'))
        return self.dist_euclidean(positions)


class HotellingGame:

    def __init__(n_firms, n_games, current_game):
        self.n_firms = n_firms
        self.n_games = n_games
        self.space = 100
        self.game = 0
        self.game_collection = []
        self.firm_collection = FirmCollection([])
        if current_game == 0
            init_states = np.linspace(self.n_firms)
            for i in range(1, self.n_firms+1):
                name = "firm_%s" % i
                setattr(self, name, Firm(init_states[i], name))
                self.firm_collection.firms.append(getattr(self, name))

    def new_game():
        self.game +=1




# %%


# %%


def calc_profits(df, space):
    """Calcula el beneficio.
    """

    try:
        lastcol = df.columns[-1]  # last game
        df = df[lastcol].copy()  # change dataframe to serie
    except:
        df = df.copy()

    # IF EACH FACTORY ARE ALONE
    if len(df.rank().unique()) == 4:  # Each player on different space
        df = df.sort_values()  # Values ordered, so index get useful
        profits = df.copy()  # make profits variable as a copy, modify after

        profits.iloc[0] = (df.iloc[0] + df.iloc[1]) / 2
        profits.iloc[1] = (df.iloc[2] - df.iloc[0]) / 2
        profits.iloc[2] = (df.iloc[3] - df.iloc[1]) / 2
        profits.iloc[3] = (2 * space - df.iloc[3] - df.iloc[2]) / 2
        return profits

    # IF TWO FACTORY ARE TOGETHER
    elif len(df.rank().unique()) == 3:  # Only two players on the same space
        df = df.sort_values()
        profits = df.copy()
        uniques = df.unique()  # get unique values
        ns = [2 * len(df[df == v]) for v in uniques]  # number of factories at the same place
        n1, n2, n3 = [df[df == v].index for v in uniques]  # name of one factory for each group

        profits.loc[n1] = (df.loc[n1].values[0] + df.loc[n2].values[0]) / ns[0]
        profits.loc[n2] = (df.loc[n3].values[0] - df.loc[n1].values[0]) / ns[1]
        profits.loc[n3] = (2 * space - df.loc[n3].values[0] - df.loc[n2].values[0]) / ns[2]
        return profits

    # IF TWO FACTORY ARE IN TWO GROUPS
    elif len(df.rank().unique()) == 2:
        df = df.sort_values()
        profits = df.copy()
        uniques = df.unique()  # get unique values
        n1, n2 = [df[df == v].index for v in uniques]  # name of one factory for each group

        profits.loc[n1] = (df.loc[n1].values[0] + df.loc[n2].values[0]) / 4
        profits.loc[n2] = (2 * space - df.loc[n2].values[0] - df.loc[n1].values[0]) / 4
        return profits


def new_game(df, space):

    import pandas as pd
    import numpy as np

    lastcol = df.columns[-1]
    space_ini = df[lastcol].copy()
    res = space_ini.copy()
    names = space_ini.index

    prof_ini = calc_profits(space_ini.copy(), space)
    step = 1

    f = open('log.txt', 'a')
    br = '\n'
    splt = '=' * 30
    str_game = "# GAME Nº %s" % (lastcol)

    print("%s%s%s%s" % (br, str_game, br, splt), file=f)
    print("## SPACE", br, file=f)
    print(space_ini, br, br, file=f)
    print("## old profits".upper(), file=f)
    print(prof_ini, br, file=f)

    for name in names:

        space_sum = space_ini.copy()
        space_sum[name] = space_sum[name] + step
        prof_sum = calc_profits(space_sum, space)

        space_subs = space_ini.copy()
        space_subs[name] = space_subs[name] - step
        prof_subs = calc_profits(space_subs, space)

        print("## WITH %s: PROFITS:" % name.upper(), br, file=f)
        print("## ini profits".upper(), file=f)
        print(prof_ini, br, file=f)
        print("### SUM", br, file=f)
        print(prof_sum, br, file=f)

        print("### SUBSTRACT", br, file=f)
        print(prof_subs, br, file=f)

        if space_subs[name] <= 0:
            space_subs[name] = 0

        elif space_sum[name] >= space:
            space_sum[name] = space

        compar_profs = pd.Series(data=[prof_sum[name],
                                       prof_subs[name],
                                       prof_ini[name]],
                                 index="sum subs ini".split())

        best = compar_profs[compar_profs == compar_profs.max()].index[0]

        if len(compar_profs.unique()) == 1:
            best = "ini"
        elif all(compar_profs - compar_profs['ini'] <= 0.4):
            compar_profs - compar_profs['ini']
            compar_profs - compar_profs['ini'] <= 0.4
            best = "ini"

        print("\n### BEST CHOICE\n", file=f)
        print("%s%s%s%s" % (br, compar_profs, br, best), file=f)
        print("^" * 30, file=f)
        print(br, file=f)

        store_spaces = {"sum": space_sum,
                        "subs": space_subs,
                        "ini": space_ini}

        res[name] = store_spaces[best][name]

    f.close()
    return res


space = 100
df = pd.DataFrame(index=("x1", "x2", "x3", "x4"))
df[0] = np.linspace(0, space-20, 4)

games = 100
for g in range(1, games + 1):
    df[g] = new_game(df, space)


df.T.plot()
plt.xlabel("Games")
plt.ylabel("Space")
sns.despine()
plt.ylim(0,100)

df.iloc[:,-1]
