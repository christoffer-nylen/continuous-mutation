SQLite format 3   @                                                                     -�� < �K�A�<                                                                                                                                                                                                  �U�tableerrorserrorsCREATE TABLE errors(
    msg_id INT, type_id INT,
    FOREIGN KEY (msg_id) REFERENCES error_msg(id),
    FOREIGN KEY (type_id) REFERENCES error_type(id),
    PRIMARY KEY (msg_id, type_id))+	? indexsqlite_autoindex_errors_1errors� !!�Ktableerror_typeerror_typeCREATE TABLE error_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, type TEXT UNIQUE )3G! indexsqlite_autoindex_error_type_1error_typeP++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)|�Gtableerror_msgerror_msgCREATE TABLE error_msg(
    id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, msg TEXT UNIQUE )1E indexsqlite_autoindex_error_msg_1error_msg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            