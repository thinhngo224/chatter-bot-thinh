# -*- coding: utf-8 -*-
from chatterbot import ChatBot

bot = ChatBot(
	"Darvis",
	logic_adaters = [
		"chatterbot.logic.MathematicalEvaluation",
		"chatterbot.logic.TimeLogicAdapter",
		"chatterbot.logic.BestMatch"
	],
	input_adapters = "chatterbot.input.TerminalAdapter",
	output_adapters = "chatterbot.output.TerminalAdapter",
	trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
)
bot.train(
	"chatterbot.corpus.custom.myown"
)
print ("type something to begin...")
while True:
	try:
		a = input()
		bot_input = bot.get_response(a)
		print (bot_input)
	except (KeyboardInterrupt, EOFError, SystemExit):
		break


