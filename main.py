#!/usr/bin/python3
from models.words import Words
from controllers.commander import Commander


helpermsg = """
////////////////////////////////////////////////////////////////////
//                          _ooOoo_                               //
//                         o8888888o                              //
//                         88" . "88                              //
//                         (| ^_^ |)                              //
//                         O\  =  /O                              //
//                      ____/`---'\____                           //
//                    .'  \\|      |//  `.                         //
//                   /  \\|||   :  |||//  \                        //
//                  /  _||||| -:- |||||-  \                       //
//                  |   | \\\  -   /// |   |                       //
//                  | \_|  ''\---/''  |   |                       //
//                  \  .-\__  `-`  ___/-. /                       //
//                ___`. .'  /--.--\  `. . ___                     //
//              ."" '<  `.___\_<|>_/___.'  >'"".                  //
//            | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 //
//            \  \ `-.   \_ __\ /__ _/   .-` /  /                 //
//      ========`-.____`-.___\_____/___.-`____.-'========         //
//                           `=---='                              //
//      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        //
//                         Ⓥⓞⓒⓐⓑⓤⓛⓐⓡⓨ                             //
////////////////////////////////////////////////////////////////////
        Type \33[1m\33[36m`help`\33[0m\33[0m to get help.
"""
helpermsg = "        Type \33[1m\33[36m`help`\33[0m\33[0m to get help."
# print(helpermsg)

#enter the main loop
commander = Commander()
commander.recite()

if  __name__ == "__main__":
    from models.history import History
    history = History()
    history.findWrongWords()