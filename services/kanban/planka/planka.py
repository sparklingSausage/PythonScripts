from plankapy import Planka, PasswordAuth

# === AUTHENTICATION ===
auth = PasswordAuth('USER', 'PASSWORD')
planka = Planka('http://example.com', auth)

# === COMPANIES ===
NUMBERS = [
    "1",
    "2",
    "3"
]

# === FUNCTIONS ===
def bulkAddTasks(PROJECT, BOARD, LIST, CARD, TASKS, DEBUG):
    project = planka.projects[PROJECT].boards[BOARD].lists[LIST].cards[CARD]

    for x in reversed(TASKS):
        project.add_task(x)
        if DEBUG:
            print("Project:", PROJECT, "Board:", BOARD, "List:", LIST, "Card:", CARD, "Task:", x)

# Just some testing to get familiar with the API
def newEverything(PROJECT, BOARD, LIST, CARD, TASK, DEBUG):
    newProject = planka.create_project(PROJECT)
    newProject.add_project_manager(planka.me)
    if DEBUG:
        print("Created Project:", PROJECT)

    createBoard = newProject.create_board(BOARD)
    if DEBUG:
        print("Created Board", BOARD)
    createList = createBoard.create_list(LIST)
    if DEBUG:
        print("Created List", LIST)
    createCard = createList.create_card(CARD)
    if DEBUG:
        print("Created Card", CARD)
    createCard.add_task("x")
    if DEBUG:
        print("Added Task:", TASK)
    
    num = [1, 2, 3, 4, 5]
    for x in num:
        createCard.add_task(x)
        if DEBUG:
            print("Added Loop Task:", x) 

# === MAIN ===
bulkAddTasks(2, 0, 0, 0, NUMBERS, 0)
#newEverything("PROJECT", "BOARD", "LIST", "CARD", "TASK", "DEBUG")