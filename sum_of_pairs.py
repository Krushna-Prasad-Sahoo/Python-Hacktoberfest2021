def sum_of_pairs(
    arr: [int], k: int
) -> bool:  # possibilty of pair with sum k is verified
    return True if [i for i in arr if k - i in arr] else False


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(
            int, input().split()
        )  # n -> no.of elements and k -> required pair sum
        arr = list(map(int, input().split()))  # list of elements
        print(sum_of_pairs(arr, k))
