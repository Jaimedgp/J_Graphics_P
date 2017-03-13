cd 

mkdir ./J_Graphics_P
mkdir ./J_Graphics_P/Front-end/
mkdir ./J_Graphics_P/Back-end/

cd ./J_Graphics_P/Front-end/
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Front-end/MainLayout.py
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Front-end/Main.py
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Front-end/MainWindow.py
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Front-end/PlotGraph.py
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Front-end/TableGUI.py

cd

cd ./J_Graphics_P/Back-end
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Back-end/Calculator.py
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Back-end/GraphPlot.py
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Back-end/OpenScrypt.py
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Back-end/SaveScrypt.py
wget https://github.com/Jaimedgp/J_Graphics_P/blob/Development/Back-end/WidgetsScrypt.py

cd

echo "alias JGP='python ./J_Graphics_P/Front-end/Main.py'" >> .bashrc