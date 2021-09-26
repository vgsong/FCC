class Rectangle:
    def __init__(self,width,height):
            self.width = width
            self.height = height

    def __str__(self):
        return f'{type(self).__name__}(width={self.width}, height={self.height})'


    def set_width(self,width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return int(self.width) * int(self.height)

    def get_perimeter(self):
        return (2*self.width) + (2*self.height)

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5

    def get_picture(self):
        # print(type(self).__name__)
        r = self.height
        c = self.width
        result = ''

        if r >= 50 or c >=50:

            return "Too big for picture."

        else:

            for x in range(0,r):
                for y in range(0,c):

                    if y+1 == c:
                        result += '*\n'
                        continue

                    result += '*'

        return result

    def get_amount_inside(self,x):
        if self.width > 50 or self.height> 50:
            return 'Invalid dimensions'
        else:
            if self.width == self.height:
                # print('squaredesu')
                return int((self.width/x.width))*(int(self.height/x.width))

            else:
                # print('rekutanguru')
                return int((self.width / x.width)) * (int(self.height / x.height))



class Square(Rectangle):

    def __init__(self,side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'{type(self).__name__}(side={self.width})'

    def set_side(self,side):
        self.width = side
        self.height = side