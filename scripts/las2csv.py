
import welly 
import argparse


parser = argparse.ArgumentParser(description='Convert las to csv')
parser.add_argument('-i', '--input', type=str, required=True, help='the input las file')
parser.add_argument('-o', '--output', type=str, required=True, help='the output csv file')


def las2df(fname):
    w = welly.Well.from_las(fname)
    df = w.df()
    return df


if __name__ == "__main__":
    args = parser.parse_args()
    df = las2df(args.input)
    df.to_csv(args.output)
