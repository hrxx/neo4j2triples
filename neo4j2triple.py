import os


def getRelations():
    os.system('echo "match (a)-[r]->(b) RETURN a.name, type(r), b.name;" > neo4j2triple.cypher')
    os.system('./neo4j-shell -file neo4j2triple.cypher > neo4j2triple-relation.temp')
    with open("neo4j2triple-relation.temp", "r") as lines:
        for line in lines:
            # print line
            eles = line.split("|")
            if len(eles) != 5:
                continue
            node1 = eles[1].strip()
            node1 = node1[1:len(node1)-1]
            relation = eles[2].strip()
            relation = relation[1:len(relation)-1]
            node2= eles[3].strip()
            node2 = node2[1:len(node2)-1]
            print node1, relation, node2
    os.system('rm neo4j2triple-relation.temp')
    os.system('rm neo4j2triple.cypher')

def getProperties():
    os.system('echo "match (n) return n.name, properties(n);" > neo4j2triple.cypher')
    os.system('./neo4j-shell -file neo4j2triple.cypher > neo4j2triple-property.temp')
    with open("neo4j2triple-property.temp", "r") as lines:
        for line in lines:
            eles = line.split("|")
            if len(eles) != 4 :
                continue
            node = eles[1].strip()
            node = node[1:len(node)-1]
            name_value = eles[2].strip()
            name_value = name_value.split("->")
            if len(name_value) != 2:
                continue
            name = name_value[0].strip()[1:]
            value = name_value[1].strip()
            value = value[:len(value)-1]
            value = value[1:len(value)-1]

            print node, name, value

    os.system('rm neo4j2triple-property.temp')
    os.system('rm neo4j2triple.cypher')

def getLabels():
    os.system('echo "match (n) return n.name, labels(n);" > neo4j2triple.cypher')
    os.system('./neo4j-shell -file neo4j2triple.cypher > neo4j2triple-label.temp')
    with open("neo4j2triple-label.temp", "r") as lines:
        for line in lines:
            eles = line.split("|")
            if len(eles) != 4:
                continue
            node = eles[1].strip()
            node = node[1:len(node)-1]
            name = "ISA"
            value = eles[2].strip()
            value = value[2:len(value)-2]
            print node, name, value
    os.system('rm neo4j2triple-label.temp')
    os.system('rm neo4j2triple.cypher')

getRelations()
getProperties()
getLabels()