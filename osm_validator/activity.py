# from . import models







    #
    # def get_data_using_id(self, id):
    #     '''
    #        data of a specific activity using its id
    #     '''
    #
    #         'SELECT * FROM Activity WHERE id=' + str(id))
    #
    #
    #
    # def get_number_of_activity(self, id):
    #     '''
    #         number of activity stored by a specific user
    #     '''
    #     'SELECT COUNT(activity) FROM notes WHERE user_id=' + str(id))
    #
    #
    #
    #
    # def get_data(self, id):
    #     '''
    #         getting data of all activity
    #     '''
    #    ('SELECT * FROM activity')
    #
    #
    #
    # def create(self):
    #     '''
    #         adding activity into the database
    #     '''
    #     "INSERT INTO activity() VALUES (?, ?, ?, ?, ?)",
    #
    #
    # def update_name(self, id):
    #     '''
    #         update activity into the database
    #     '''
    #    "UPDATE activity SET"
    #
    #
    # def delete(self, id):
    #     '''
    #            deleting a specific activity using its id
    #     '''
    #     "DELETE FROM activity WHERE id=" + str(id))
            

def main():
        menu = None
        while menu != "Q":

            print\
                (
                    """
                    Menu
                    
                    Q - Quit
                    L - List of activities with id
                    G - Get one activity on id
                    C - Create
                    U - Update 
                    D - Delete
                    """
                )
            menu = input("Enter the sign ")

            if menu == "Q":
                print("Quit")
            elif menu == "L":
                a = input('')
                print('List')
                # Activity.()
            elif menu == "G":
                print('a')
                # Activity.
            elif menu == "C":
                print('a')
                # Activity.
            elif menu == "U":
                print('a')
                # Activity.
            elif menu == "D":
                print('a')
                # Activity.

            else:
                print("No such signs")

main()