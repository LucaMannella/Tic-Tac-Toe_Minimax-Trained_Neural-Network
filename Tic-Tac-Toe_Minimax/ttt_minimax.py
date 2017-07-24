#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#################################################################################################
#  _____ _          _____               _____                                         __    __  #
# /__   (_) ___    /__   \__ _  ___    /__   \___   ___      /\/\    /\/\          /\ \ \/\ \ \ #
#   / /\/ |/ __| __  / /\/ _` |/ __| __  / /\/ _ \ / _ \    /    \  /    \  ____  /  \/ /  \/ / #
#  / /  | | (__ (__)/ / | (_| | (__ (__)/ / | (_) |  __/   / /\/\ \/ /\/\ \(____)/ /\  / /\  /  #
#  \/   |_|\___|    \/   \__,_|\___|    \/   \___/ \___|   \/    \/\/    \/      \_\ \/\_\ \/   #
#                                                                                               #
# (c) July 2017 by Luca Mannella                                                                #
# Tic-Tac-Toe MM-NN is distributed under GNU GENERAL PUBLIC LICENSE v.3                         #
#                                                                                               #
#################################################################################################

import logging

VERSION = "v0.1"


def main():
    """ That's Main! """
    pass


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s")
    logging.getLogger().setLevel(level=logging.INFO)
    logging.info(r"         _       _                          _____           _       _    (!) %s    ", VERSION)
    logging.info(r"   /\/\ (_)_ __ (_)_ __ ___   __ ___  __   /__   \_ __ __ _(_)_ __ (_)_ __   __ _  ")
    logging.info(r"  /    \| | '_ \| | '_ ` _ \ / _` \ \/ /____ / /\/ '__/ _` | | '_ \| | '_ \ / _` | ")
    logging.info(r" / /\/\ \ | | | | | | | | | | (_| |>  <_____/ /  | | | (_| | | | | | | | | | (_| | ")
    logging.info(r" \/    \/_|_| |_|_|_| |_| |_|\__,_/_/\_\    \/   |_|  \__,_|_|_| |_|_|_| |_|\__, | ")
    logging.info(r"  Developed by Luca Mannella - July 2017                                    |___/  ")

    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", datefmt="%H:%M:%S")
    logging.getLogger().setLevel(level=logging.DEBUG)
    logging.getLogger().handlers[0].setFormatter(logging.Formatter(
        "%(asctime)s.%(msecs)04d %(levelname)s: %(message)s", datefmt="%H:%M:%S"))

    main()
