def main():
    import sys

    animals = 'herd of elephants'
    x, y = 1, 1
    seg = animals[x:y]
    print('Segment is:', seg)

    def segPrint():
        seg = animals[x:y]
        if len(seg) > 0:
            print(seg, f"- where x = {x} and y = {y}")

    def segPrintX():
        seg = animals[x:]
        print(seg, f"- where x = {x} and y is omitted")

    def segPrintY():
        seg = animals[:y]
        print(seg, f"- where x is omitted and y = {y}")

    original_stdout = sys.stdout # Save a reference to the original standard output
    with open('p2p5.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        #(a) What happens when x and y are the same?
        for i in range(17):
            x, y = i, i
            segPrint()

        # (b) What happens when x is greater than y?
        for x in range(17):
            for y in range(17):
                segPrint()

        # (c) What happens when x is omitted?
        for y in range(17):
            segPrintY()

        # (d) What happens when y is omitted?
        for x in range(17):
            segPrintX()

        # (e) What happens when both x and y are omitted?
        seg = animals[:]
        print(seg, f"- where x and y are omitted")

        sys.stdout = original_stdout # Reset the standard output to its original value

if __name__ == "__main__":
    main()