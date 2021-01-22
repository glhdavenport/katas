class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def is_valid(self):
        current_length = None
        for row in self.rectangle:
            if current_length is None:
                current_length = len(row)
            if len(row) != current_length:
                return False
        return True

    def get_value(self, x, y):
        return self.rectangle[x][y]

    def update_subrectangle(self, r1, c1, r2, c2, new_value):
        for row_index in range(len(self.rectangle)):
            for col_index in range(len(self.rectangle[row_index])):
                if r1 <= row_index <= r2 and c1 <= col_index <= c2: 
                    self.rectangle[row_index][col_index] = new_value
        
        """
        [
            [0, 1, 2],        r1
            [3, 4, 5],        r2
            [6, 7, 8]         r3
        ]

            c1 c2 c3

        """


# ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
# [
#     [
#         [
#             [1,2,1],
#             [4,3,4],
#             [3,2,1],
#             [1,1,1]
#         ]
#     ],
#     [0,2],
#     [0,0,3,2,5],
#     [0,2],
#     [3,1],
#     [3,0,3,2,10],
#     [3,1],
#     [0,2]
# ]
# Output
# [null,1,null,5,5,null,10,5]