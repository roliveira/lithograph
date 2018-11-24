
import welly 


def las2df(fname):
    w = welly.Well.from_las(fname)
    df = w.df()
    return df

