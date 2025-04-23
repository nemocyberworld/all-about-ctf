cypher = // include here the long string from netcat then extract the flag from first line, from hex to ascii
for x in range(len(cypher)):
    print(cypher[x][0], cypher[x][-1], end="")