import sqlite3
import os

class DB:
    __connection = None
    __cursor = None
    
    def __init__(self, db: str):
        self.db = db
        
    def connect(self):
        if not self.__connection:
            self.__connection = sqlite3.connect(self.db)
            self.__cursor = self.__connection.cursor()
            self.__cursor.execute(""" PRAGMA foreign_key = ON """)
            
    def close(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None
            self.__cursor = None
            
    def dropDB(self):
        if os.path.exists(self.db):
            os.remove(self.db)
            
    def createTables(self):
        ## Create Groups Table
        query = """ CREATE TABLE IF NOT EXISTS `groups` (
                        
                        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        `name` TEXT NOT NULL
                            
                ); """
        self.__cursor.execute(query)
        
        ## Create Students Table
        query = """ CREATE TABLE IF NOT EXISTS `students` (
                        
                        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        `name` TEXT NOT NULL,
                        `year` INTEGER NOT NULL,
                        `groups_id` INTEGER,
                        FOREIGN KEY (`groups_id`) REFERENCES `groups` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
                            
                ); """
        self.__cursor.execute(query)
        
        ## Create Teachers Table
        query = """ CREATE TABLE IF NOT EXISTS `teachers` (
                        
                        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        `name` TEXT NOT NULL
                            
                ); """
        self.__cursor.execute(query)
        
        ## Create Courses Table
        query = """ CREATE TABLE IF NOT EXISTS `courses` (
                        
                        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        `name` TEXT NOT NULL,
                        `hours` INTEGER,
                        `teachers_id` INTEGER,
                        FOREIGN KEY (`teachers_id`) REFERENCES `teachers` (`id`)
                            
                ); """
        self.__cursor.execute(query)
        
        ## Create linkage table
        query = """ CREATE TABLE IF NOT EXISTS `groups_has_courses` (
                    `groups_id` INTEGER,
                    `courses_id` INTEGER,
                    FOREIGN KEY (`groups_id`) REFERENCES `groups` (`id`),
                    FOREIGN KEY (`courses_id`) REFERENCES `courses` (`id`)
                    )"""
                    
        self.__cursor.execute(query)
        
    def seedData(self, groups: list, students: list, teachers: list, courses: list, groups_courses: list):
            query = """ INSERT INTO `groups` (`name`) VALUES (?) """
            self.__cursor.executemany(query, groups)
            
            query = """ INSERT INTO `students` (`name`, `year`, `groups_id`) VALUES (?, ?, ?)"""
            self.__cursor.executemany(query, students)
            
            query = """ INSERT INTO `teachers` (`name`) VALUES (?)"""
            self.__cursor.executemany(query, teachers)
            
            query = """ INSERT INTO `courses` (`name`, `hours`, `teachers_id`) VALUES (?, ?, ?)"""
            self.__cursor.executemany(query, courses)
            
            query = """ INSERT INTO `groups_has_courses` (`groups_id`, `courses_id`) VALUES (?, ?)"""
            self.__cursor.executemany(query, groups_courses)
            
            
            self.__connection.commit()
            
    def selectGroups(self):
        query = """ SELECT `id`, `name` FROM `groups`;"""
        self.__cursor.execute(query)
        groups = self.__cursor.fetchall()
        
        return groups
    
    def selectStudents(self, group: str = None):
        if group:
            query = """ SELECT `groups`.`name`, `students`.`name`, `students`.`year` FROM `groups`
                        JOIN `students` ON `groups`.`id` = `students`.`groups_id`
                        WHERE `groups`.`name` = ?; """
            self.__cursor.execute(query, (group,))
        else:
            query = """ SELECT `id`, `name`, `year` FROM `students`; """
            self.__cursor.execute(query)
            
        data = self.__cursor.fetchall()
        
        return data
            

    def selectCourses(self, group: str):
        query = """ SELECT `courses`.`name`, `teachers`.`name` FROM `groups`
                    JOIN `groups_has_courses` ON `groups`.`id` = `groups_has_courses`.`groups_id`
                    JOIN `courses` ON `groups_has_courses`.`courses_id` = `courses`.`id`
                    JOIN `teachers` ON `courses`.`teachers_id` = `teachers`.`id`
                    WHERE `groups`.`name` = ?;"""
        self.__cursor.execute(query, (group,))
        data = self.__cursor.fetchall()
        return data