import graphics
import os

def main():
	windowName = "Anime Renaming Utility ~ (A.R.U.)"
	windowX = 400
	windowY = 400
	window = graphics.GraphWin(windowName, windowX, windowY)
	window.setBackground(graphics.color_rgb(17, 17, 29))

	lineX = graphics.Line(graphics.Point(0, 280), graphics.Point(400, 280))
	lineX.setFill("white")
	lineX.draw(window)
	lineY = graphics.Line(graphics.Point(130, 0), graphics.Point(130, 400))
	lineY.setFill("white")
	lineY.draw(window)

	base_folder = os.path.dirname(__file__)
	left_path = os.path.join(base_folder, 'assets/leftarrow.gif')
	right_path = os.path.join(base_folder, 'assets/rightarrow.gif')

	nameLabel = graphics.Text(graphics.Point(60, 40), "Name:")
	nameControl = graphics.Entry(graphics.Point(260, 40), 25)
	seasonLabel = graphics.Text(graphics.Point(60, 100), "Season:")
	seasonControl = graphics.Entry(graphics.Point(160, 100), 3)
	episodesLabel = graphics.Text(graphics.Point(60, 160), "Episodes:")
	episodesControl = graphics.Entry(graphics.Point(160, 160), 3)
	startLabel = graphics.Text(graphics.Point(60, 220), "RENAME")
	startButton = graphics.Rectangle(graphics.Point(20, 205), graphics.Point(100, 235))
	resultLabel = graphics.Text(graphics.Point(60, 340), "0 of 0:")
	resultControl = graphics.Entry(graphics.Point(260, 340), 25)
	leftButton = graphics.Rectangle(graphics.Point(5, 370), graphics.Point(30, 395))
	rightButton = graphics.Rectangle(graphics.Point(100, 370), graphics.Point(125, 395))
	leftLabel = graphics.Image(graphics.Point(17.5, 382.5), left_path)
	rightLabel = graphics.Image(graphics.Point(112.5, 382.5), right_path)
	
	nameLabel.setTextColor("white")
	nameControl.setFill("white")
	seasonLabel.setTextColor("white")
	seasonControl.setFill("white")
	episodesLabel.setTextColor("white")
	episodesControl.setFill("white")
	startLabel.setTextColor("white")
	startButton.setFill("green")
	resultLabel.setTextColor("white")
	resultControl.setText(' (^~^;)/   "Ready to go!"')
	leftButton.setFill(graphics.color_rgb(17, 17, 29))
	rightButton.setFill(graphics.color_rgb(17, 17, 29))
	leftButton.setOutline(graphics.color_rgb(17, 17, 29))
	rightButton.setOutline(graphics.color_rgb(17, 17, 29))

	seasonLabel.draw(window)
	seasonControl.draw(window)
	episodesLabel.draw(window)
	episodesControl.draw(window)
	startButton.draw(window)
	startLabel.draw(window)
	resultLabel.draw(window)
	resultControl.draw(window)
	nameLabel.draw(window)
	nameControl.draw(window)

	name = ""
	season = 0
	episodes = 0
	clearMode = False
	displayed = 0

	while True:
		click = window.checkMouse()
		key = window.checkKey()

		if detect_start(startButton, click, key):
			if clearMode:
				nameControl.setText("")
				seasonControl.setText("")
				episodesControl.setText("")
				resultControl.setText("")

				displayed = 0
				episodes = 0
				resultLabel.setText(str(displayed) + " of " + str(episodes))
				resultControl.setText(' (^~^;)/   "Ready to go!"')

				leftButton.undraw()
				rightButton.undraw()
				leftLabel.undraw()
				rightLabel.undraw()

				startButton.undraw()
				startLabel.undraw()
				startButton.setFill("green")
				startLabel.setText("RENAME")
				startButton.draw(window)
				startLabel.draw(window)

				clearMode = False
			else:
				startButton.undraw()
				startLabel.undraw()
				startButton.setFill("red")
				startLabel.setText("CLEAR")
				startButton.draw(window)
				startLabel.draw(window)

				leftButton.draw(window)
				rightButton.draw(window)
				leftLabel.draw(window)
				rightLabel.draw(window)

				name = nameControl.getText()
				season = seasonControl.getText()
				episodes = get_episodes(episodesControl)

				if int(episodes) > 0:
					displayed = displayed + 1

				resultLabel.setText(str(displayed) + " of " + str(episodes))
				clearMode = True

		if clearMode:
			if detect_left(leftButton, click, key) and displayed > 1:
				displayed = displayed - 1
			elif detect_right(rightButton, click, key) and displayed < int(episodes):
				displayed = displayed + 1

			if name == '' and season == '' and episodes == '0':
				resultControl.setText(' (o_o*)    "Umm..."')
			elif name == '':
				resultControl.setText(' (~_~;)    "Name, baka!"')
			elif episodes == '0':
				resultControl.setText(' (~_~;)    "Episodes, baka!!"')
			else:
				result = format(name, season, displayed)

				resultLabel.setText(str(displayed) + " of " + str(episodes))
				resultControl.setText(result)

	return


def detect_start(button, click, key):
	if click:
		cX = click.getX()
		cY = click.getY()
		bX1 = button.getP1().getX()
		bX2 = button.getP2().getX()
		bY1 = button.getP1().getY()
		bY2 = button.getP2().getY()
		if bX1 < cX < bX2 and bY1 < cY < bY2:
			return True

	if key == 'Return':
		return True

	return False


def detect_left(button, click, key):
	if click:
		cX = click.getX()
		cY = click.getY()
		bX1 = button.getP1().getX()
		bX2 = button.getP2().getX()
		bY1 = button.getP1().getY()
		bY2 = button.getP2().getY()
		if bX1 < cX < bX2 and bY1 < cY < bY2:
			return True
		return False


def detect_right(button, click, key):
	if click:
		cX = click.getX()
		cY = click.getY()
		bX1 = button.getP1().getX()
		bX2 = button.getP2().getX()
		bY1 = button.getP1().getY()
		bY2 = button.getP2().getY()
		if bX1 < cX < bX2 and bY1 < cY < bY2:
			return True
		return False


def get_episodes(control):
	episodes = control.getText()
	if episodes == '' or int(episodes) < 1:
		return '0'

	return episodes


def format(name, season, episode):
	dash = ' - '

	if season:
		season = int(season)
		seasonTag = 'S'
		episodeTag = 'E'
		space = ' '

		if season < 10:
			season = '0' + str(season)
		else:
			season = str(season)
	else:
		seasonTag = ''
		episodeTag = ''
		space = ''

	if episode < 10:
		episode = '0' + str(episode)
	else:
		episode = str(episode)

	return name + dash + seasonTag + season + space + episodeTag + episode


main()
