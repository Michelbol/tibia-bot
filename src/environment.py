import os

class Environment:
    PATH_WINDOWS = 'C:/Users/miche/AppData/Local/Tibia/packages/Tibia/screenshots/'
    PATH_LINUX = '/home/michel.reis@db1.com.br/.local/share/CipSoft GmbH/Tibia/packages/Tibia/screenshots/'
    HEADER_ANALYSER_PC_DB1 = {
        'life': {
            'x': 380,
            'y': 0,
            'h': 20,
            'w': 100,
            'config_tesseract': '--tessdata-dir tessdata --psm 13'
        },
        'mana': {
            'x': 1800,
            'y': 100,
            'h': 60,
            'w': 100,
            'config_tesseract': '--tessdata-dir tessdata --psm 13'
        },
    }
    HEADER_ANALYSER_NOTEBOOK = {
        'life': {
            'x': 360,
            'y': 0,
            'h': 20,
            'w': 100,
            'config_tesseract': '--tessdata-dir tessdata --psm 11'
        },
        'mana': {
            'x': 770,
            'y': 0,
            'h': 20,
            'w': 100,
            'config_tesseract': '--tessdata-dir tessdata --psm 6'
        },
    }
    RIGHT_HEALTH_BAR_PC_DB1 = {
        'life': {
            'x': 1790,
            'y': 118,
            'h': 14,
            'w': 100,
            'config_tesseract': '--tessdata-dir tessdata --psm 13'
        },
        'mana': {
            'x': 1790,
            'y': 131,
            'h': 14,
            'w': 100,
            'config_tesseract': '--tessdata-dir tessdata --psm 13'
        },
    }

    RIGHT_HEALTH_BAR_NOTEBOOK = {
        'life': {
            'x': 1310,
            'y': 118,
            'h': 14,
            'w': 100,
            'config_tesseract': '--tessdata-dir tessdata --psm 13'
        },
        'mana': {
            'x': 1310,
            'y': 131,
            'h': 14,
            'w': 100,
            'config_tesseract': '--tessdata-dir tessdata --psm 13'
        },
    }

    HEADER_LEVEL_BAR_PC_DB1 = {
        'level': {
            'x': 200,
            'y': 20,
            'h': 14,
            'w': 50,
            'config_tesseract': '--tessdata-dir tessdata --psm 13'
        },
    }

    HEADER_LEVEL_BAR_NOTEBOOK = {
        'level': {
            'x': 110,
            'y': 22,
            'h': 14,
            'w': 50,
            'config_tesseract': '--tessdata-dir tessdata --psm 13'
        },
    }

    SKILLS_WINDOW_PC_DB1 = {
        'default': {
            'x': 100,
            'h': 16,
            'w': 60,
            'config_tesseract': '--tessdata-dir tessdata --psm 13',
            'y': None
        },
        'position': {
            'level': 18,
            'experience': 40,
            'xp-rate': 52,
            'life': 83,
            'mana': 100,
            'soul': 116,
            'capacity': 130,
            'speed': 144,
            'food': 158,
            'stamina': 172,
            'magic-level': 225,
        }
    }

    SKILLS_WINDOW_NOTEBOOK = {
        'default': {
            'x': 100,
            'h': 21,
            'w': 60,
            'config_tesseract': '--tessdata-dir tessdata --psm 13',
            'y': None
        },
        'position': {
            'level': 22,
            'experience': 40,
            'xp-rate': 52,
            'life': 83,
            'mana': 100,
            'soul': 114,
            'capacity': 128,
            'speed': 140,
            'food': 158,
            'stamina': 172,
            'magic-level': 223,
        }
    }

    BATTLE_CONFIG_DB1 = {
        'x': 1675,
        'y': 463,
        'h': 60,
        'w': 180,
        'config_tesseract': '--tessdata-dir tessdata --psm 13',
    }

    BATTLE_MONSTERS_DB1 = {
        'y': 1,
        'h': 22
    }

    BATTLE_CONFIG_NOTEBOOK = {
        'x': 1190,
        'y': 547,
        'h': 60,
        'w': 180,
        'config_tesseract': '--tessdata-dir tessdata --psm 13',
    }

    BATTLE_MONSTERS_NOTEBOOK = {
        'y': 1,
        'h': 22
    }


    def isWindows():
        return os.name != 'posix'

    def resolveScreenshotsPath():
        if(Environment.isWindows()):
            return Environment.PATH_WINDOWS
        return Environment.PATH_LINUX

    def resolveHeaderAnalyser():
        if(Environment.isWindows()):
            return Environment.HEADER_ANALYSER_NOTEBOOK
        return Environment.HEADER_ANALYSER_PC_DB1
    
    def resolveRightHealthBar():
        if(Environment.isWindows()):
            return Environment.RIGHT_HEALTH_BAR_NOTEBOOK
        return Environment.RIGHT_HEALTH_BAR_PC_DB1
    
    def resolveHeaderLevelBar():
        if(Environment.isWindows()):
            return Environment.HEADER_LEVEL_BAR_NOTEBOOK
        return Environment.HEADER_LEVEL_BAR_PC_DB1
    
    def resolveSkillsWindow():
        if(Environment.isWindows()):
            return Environment.SKILLS_WINDOW_NOTEBOOK
        return Environment.SKILLS_WINDOW_PC_DB1
    
    def resolveBattleConfigs():
        if(Environment.isWindows()):
            return Environment.BATTLE_CONFIG_NOTEBOOK
        return Environment.BATTLE_CONFIG_DB1
    
    def resolveBattleMonsterConfigs():
        if(Environment.isWindows()):
            return Environment.BATTLE_MONSTERS_NOTEBOOK
        return Environment.BATTLE_MONSTERS_DB1
    
    def isProduction():
        return Environment.isWindows()