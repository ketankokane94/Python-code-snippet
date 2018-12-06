
from graph import Graph


def set_maze_dimensions(line):
    '''
    this function sets the required dimensions of the maze
    :param line:
    :return:
    '''
    line = line.split(' ')
    global NO_OF_ROWS
    global NO_OF_COLS
    global ESCAPE_ROW
    NO_OF_ROWS = int(line[0])
    NO_OF_COLS = int(line[1])
    ESCAPE_ROW = int(line[2])


def create_vertex(graph, row_number, line):
    '''
    function which takes a line read from file and decides wheather to create a vertex of it or no
    :param graph:
    :param row_number:
    :param line:
    :return:
    '''
    for index in range(len(line)):
        if line[index] is '.':
            graph.addVertex(str(index) + ',' + str(row_number) )


def read_maze_from_file(graph, filename = 'test.txt'):
    '''
    this function is responsible for reading the text file which contains the maze and calls appropriate function to
    start creating the graph required to solve the maze
    :param graph:
    :param filename:
    :return:
    '''
    # variable to track if the first line is read or not
    first_line_read = False
    # row number to keep track of the naming of the vertex
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
    '''
    add neighbours to the given vertex on the same row
    :param vertex:
    :param maze:
    :return:
    '''
    rows(vertex.id.split(',')[1], vertex, maze)


def anything_to_left(vertex, maze):
    '''
    function which if there is anything to the left side of the given vertex
    it could either have a wall or rock or nothing
    appropriate actions are taken based on it
    :param vertex:
    :param maze:
    :return:
    '''
    if vertex is None:
        return 'node'
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
            return 'node'
    else:
        # has wall
        return 'wall'


def anything_to_right(vertex, maze):
    '''
    function which if there is anything to the right side of the given vertex
    it could either have a wall or rock or nothing
    appropriate actions are taken based on it
    :param vertex:
    :param maze:
    :return:
    '''
    if vertex is None:
        return 'node'
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
            return 'node'
    else:
        # has wall
        return 'wall'


def anything_to_top(vertex, maze):
    '''
    function which if there is anything to the left side of the given vertex
    it could either have a wall or rock or nothing
    appropriate actions are taken based on it
    :param vertex:
    :param maze:
    :return:
    '''
    if vertex is None:
        return 'node'
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
            return 'node'
    else:
        # has wall
        return 'wall'


def anything_below(vertex, maze):
    '''
    function which if there is anything to the below side of the given vertex
    it could either have a wall or rock or nothing
    appropriate actions are taken based on it
    :param vertex:
    :param maze:
    :return:
    '''
    if vertex is None:
        return 'node'
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
            return 'node'
    else:
        # has wall
        return 'wall'


def check_if_vertex_has_anything_on_left(vertex, maze,output_list):
    to_left = anything_to_left(vertex, maze)

    if to_left is 'rock' :
        # add nodes which are to the right side of the current node
        for _ in range(int(vertex.id.split(',')[0])+1,NO_OF_COLS):
            node = maze.getVertex(str(_)+ ','+ vertex.id.split(',')[1])
            if node is None:
                break
            elif node.id not in output_list:
                vertex.addNeighbor(node, 1)
                output_list.append(node.id)


def check_if_vertex_has_anything_on_right(vertex, maze,output_list):
    to_right = anything_to_right(vertex, maze)

    if to_right is 'rock' or to_right is 'wall':
        # add nodes which are to the right side of the current node
        for _ in range(int(vertex.id.split(',')[0]) - 1, -1, -1):
            node = maze.getVertex(str(_) + ',' + vertex.id.split(',')[1])
            if node is None:
                break
            elif node.id not in output_list:
                vertex.addNeighbor(node, 1)
                output_list.append(node.id)


def check_if_vertex_has_anything_on_top(vertex, maze,output_list):
    above = anything_to_top(vertex, maze)

    if above is 'rock' or above is 'wall':
        # add nodes which are to the bottom of the current node
        for _ in range((int(vertex.id.split(',')[1]) + 1),
                       NO_OF_ROWS):
            node = maze.getVertex(vertex.id.split(',')[0] + ',' + str(_))
            if node is None:
                break
            elif node.id not in output_list:
                vertex.addNeighbor(node, 1)
                output_list.append(node.id)


def check_if_vertex_has_anything_on_bottom(vertex, maze,output_list):
    below = anything_below(vertex, maze)

    if below is 'rock' or below is 'wall':
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
        else:
            break


def __findPathDFS(current, end, visited):
    """
    Private recursive helper function that finds the path, if one exists,
    from the current vertex to the end vertex
    :param current (Vertex): The current vertex in the traversal
    :param end (Vertex): The destination vertex
    :param visited (set of Vertex): the vertices already visited
    :return: A list of Vertex objects from start to end, if a path exists,
        otherwise None
    """

    # A successful base case is when we traverse to the end vertex.  In this
    # case, wrap it in a list and return it to the caller to construct the
    # full path
    if current == end:
        return [current]
    for neighbor in current.getConnections():
        if neighbor not in visited:
            visited.add(neighbor)
            path = __findPathDFS(neighbor, end, visited)
            # If the path is not None, current is part of the solution path,
            # so add it to the front of the path list and return it
            if path != None:
                path.insert(0, current)
                return path
    # No path was found, so pass back None
    return None

def findPathDFS(start, end):
    """
    Find a path, if one exists, from a start to end vertex.
    :param start (Vertex): the start vertex
    :param end (Vertex): the destination vertex
    :return: A list of Vertex objects from start to end, if a path exists,
        otherwise None
    """
    visited = set()
    visited.add(start)
    return __findPathDFS(start, end, visited)


def get_path_every_bode_to_escape(maze, escape):
    paths = {'cannot escape': []}

    for node in maze.getVertices():
        if node is not escape:
            path = findPathDFS(escape, maze.getVertex(node))
            if path is not None:
                if len(path) - 1 in paths:
                    lst = paths[len(path) - 1]
                    lst.append(node)
                    paths[len(path) - 1] = lst
                else:
                    paths[len(path) - 1] = [node]
            else:
                lst = paths['cannot escape']
                lst.append(node)
                paths['cannot escape'] = lst
    return paths


def test():
    maze = Graph()

    print('test maze reading')
    read_maze_from_file(maze,'test.txt')


    # create escape node
    maze.addVertex('escape')

    escape = maze.getVertex('escape')
    # connect vertices on escape node
    add_vertexes_on_escape_row(maze,escape)

    output_list = []

    for ele in escape.getConnections():
        output_list.append(ele.id)

    print(output_list)

    for node in escape.getConnections():
        add_connections(maze,node,output_list)

    print(output_list)

    print(len(output_list))

    paths = get_path_every_bode_to_escape(maze,escape)

    for key in paths.keys():
        print(key, paths[key])

    print('---------- output ---------')
    for index in range(1,len(paths.keys())):

        if index in paths.keys() and paths[index] is not None or []:
            print(index,paths[index])

    if paths['cannot escape'] is not None:
        print('cannot escape',paths['cannot escape'])


if __name__ == '__main__':
    test()
