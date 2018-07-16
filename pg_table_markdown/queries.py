def build_schema_query(table_schema):
    schema_query = """
    SELECT      a.table_name,
                a.column_name,
                a.column_default,
                a.is_nullable,
                a.data_type,
                a.character_maximum_length,
                (
    		        SELECT pg_catalog.col_description(c.oid, a.ordinal_position::int)
        	        FROM pg_catalog.pg_class c
        	        WHERE c.oid     = (SELECT a.table_name::regclass::oid) and c.relname = a.table_name
    	        ) as desctiption
    FROM        information_schema.columns a
    WHERE       table_schema = '{0}'
    ORDER BY    table_name,
                ordinal_position
    """.format(table_schema)
    return schema_query
