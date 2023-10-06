#include "hash_tables.h"

hash_table_t *hash_table_create(unsigned long int size)
{
    hash_table_t *table;
    unsigned long int i;
    
    /*Allocate memory for the table and check if mallocing failed*/
    table = malloc(sizeof(hash_table_t));
    if (table == NULL)
    {
        
        return NULL;
    }
    /*set size of table*/
    table->size = size;
    /*Allocate memory to hold the hash nodes(elements)*/
    table->array = calloc(sizeof(hash_node_t *), table->size);
    /*size of each element and total number of element*/
    if (table->array == NULL)
    {
        free(table);
        return NULL;
    }

    
    for (i = 0; i < table->size; i++)
    {
        /*initialize all element of table to Null*/
        table->array[i] = NULL;
    }
    return table;

}