
from graph import Graph


def set_maze_dimensions(line):
    line = line.split(' ')
    global NO_OF_ROWS
    global NO_OF_COLS
    global ESCAPE_ROW
    NO_OF_ROWS = int(line[0])
    NO_OF_COLS = int(line[1])
    ESCAPE_ROW = int(line[2])


def create_vertex(graph, row_number, line,):
    for index in range(len(line)):
        if line[index] is '.':
            graph.addVertex(str(index) + ',' + str(row_number) )


def read_maze_from_file(graph, filename = 'test.txt'):
    first_line_read = False
    row_number = 0
    with open(filename) as maze:
        for line in maze:
            line = line.strip()
            if not first_line_read:
                first_line_read = True
                set_maze_dimensions(line)
            else:
                create_vertex(graph,row_number,line.split(' '))
                row_number += 1


def rows(row,v,maze):
    list = maze.getVertices()
    for ele in list:
        elem = ele.split(',')
        if elem[1] is row:
            v.addNeighbor(ele,1)


def add_neighbours_on_same_row_of_given_vertex(vertex, maze):
    rows(vertex.id.split(',')[1], vertex, maze)


def anything_to_left(vertex, maze):
    if vertex is None:
        return None
    row_num = int(vertex.id.split(',')[1])
    col_num = int(vertex.id.split(',')[0])
    col_num -= 1
    if col_num >= 0:
        left_vertex = maze.getVertex(str(col_num) + ',' + str(row_num))
        if left_vertex is None:
            #has rock
            return 'rock'
        else:
            # has some node
            return None
    else:
        # has wall
        return 'wall'


def anything_to_right(vertex, maze):
    if vertex is None:
        return None
    row_num = int(vertex.id.split(',')[1])
    col_num = int(vertex.id.split(',')[0])
    col_num += 1
    if col_num < NO_OF_COLS:
        right_vertex = maze.getVertex(str(col_num) + ',' + str(row_num))
        if right_vertex is None:
            # has rock
            return 'rock'
        else:
            # has some node
            return None
    else:
        # has wall
        return 'wall'


def anything_to_top(vertex, maze):
    if vertex is None:
        return None
    row_num = int(vertex.id.split(',')[1])
    col_num = int(vertex.id.split(',')[0])
    row_num -= 1
    if row_num >= 0:
        left_vertex = maze.getVertex(str(col_num) + ',' + str(row_num))
        if left_vertex is None:
            # has rock
            return 'rock'
        else:
            # has some node
            return None
    else:
        # has wall
        return 'wall'


def anything_below(vertex, maze):
    if vertex is None:
        return None
    row_num = int(vertex.id.split(',')[1])
    col_num = int(vertex.id.split(',')[0])
    row_num += 1
    if row_num < NO_OF_ROWS:
        left_vertex = maze.getVertex(str(col_num) + ',' + str(row_num))
        if left_vertex is None:
            # has rock
            return 'rock'
        else:
            # has some node
            return None
    else:
        # has wall
        return 'wall'


def check_if_vertex_has_anything_on_left(vertex, maze,output_list):
    to_left = anything_to_left(vertex, maze)
    if to_left is 'rock':
        # add nodes which are to the right side of the current node
        for _ in range(int(vertex.id.split(',')[0])+1,NO_OF_COLS):
            node = maze.getVertex(str(_)+ ','+ vertex.id.split(',')[1])
            if node is None:
                break
            elif node.id not in output_list:
                vertex.addNeighbor(node, 1)
                output_list.append(node.id)
    elif to_left is 'wall':
        pass


def check_if_vertex_has_anything_on_right(vertex, maze,output_list):
    to_right = anything_to_right(vertex, maze)

    if to_right is 'rock':
        # add nodes which are to the right side of the current node
        for _ in range(int(vertex.id.split(',')[0]) - 1, -1, -1):
            node = maze.getVertex(str(_) + ',' + vertex.id.split(',')[1])
            if node is None:
                break
            elif node.id not in output_list:
                vertex.addNeighbor(node, 1)
                output_list.append(node.id)
    elif to_right is 'wall':
        pass


def check_if_vertex_has_anything_on_top(vertex, maze,output_list):
    above = anything_to_top(vertex, maze)

    if above is 'rock':
        # add nodes which are to the bottom of the current node
        for _ in range((int(vertex.id.split(',')[1]) + 1),
                       NO_OF_ROWS):
            node = maze.getVertex(vertex.id.split(',')[0] + ',' + str(_))
            if node is None:
                break
            elif node.id not in output_list:
                vertex.addNeighbor(node, 1)
                output_list.append(node.id)
    elif above is 'wall':
        pass


def check_if_vertex_has_anything_on_bottom(vertex, maze,output_list):
    below = anything_below(vertex, maze)

    if below is 'rock':
        # add nodes which are to above of the current
        # node
        for _ in range((int(vertex.id.split(',')[1]) - 1),
                       -1, -1):
            node = maze.getVertex(
                vertex.id.split(',')[0] + ',' + str(_))
            if node is None:
                break
            elif node.id not in output_list:
                vertex.addNeighbor(node, 1)
                output_list.append(node.id)
    elif below is 'wall':
        pass


def add_connections(maze, vertex,output_list):
    check_if_vertex_has_anything_on_left(vertex,maze,output_list)
    check_if_vertex_has_anything_on_right(vertex,maze,output_list)
    check_if_vertex_has_anything_on_top(vertex,maze,output_list)
    check_if_vertex_has_anything_on_bottom(vertex,maze,output_list)

    if vertex is not None:
        for node in vertex.getConnections():
            add_connections(maze, node, output_list)


def add_vertexes_on_escape_row(maze, escape):
    # maze escape is always on the last column
    col = NO_OF_COLS - 1
    row = ESCAPE_ROW
    for _ in range(col, -1 ,-1 ):
        node = maze.getVertex(str(_)+ ','+ str(row))
        if node is not None:
            escape.addNeighbor(node,1)


def test():
    maze = Graph()

    print('test maze reading')
    read_maze_from_file(maze,'test.txt')


    # create escape node
    maze.addVertex('escape')

    escape = maze.getVertex('escape')
    # connect vertices on escape node
    add_vertexes_on_escape_row(maze,escape)
    #add_neighbours_on_same_row_of_given_vertex(escape, maze)

    output_list = []

    for ele in escape.getConnections():
        output_list.append(ele.id)

    print(output_list)
    '''
    #check_if_vertex_has_anything_on_bottom(maze.getVertex('1,3'),maze,
                                           output_list)
                                           '''
    for node in escape.getConnections():
        add_connections(maze,node,output_list)

    print(output_list)



if __name__ == '__main__':
    test()
