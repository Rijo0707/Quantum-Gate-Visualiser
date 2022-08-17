from qiskit import QuantumCircuit
import qiskit
from qiskit.visualization import visualize_transition
import numpy as np
import qiskit
import tkinter
import warnings

root=tkinter.Tk()
root.title("Visualizing Quantum Gates")

root.iconbitmap(default='microprocessor.ico')
root.geometry('399x410')
root.resizable(0,0) #Blocking resizing

background='#FFF9CA'
buttons='#FFB4B4'
special_buttons='#B2A4FF'
button_font=('Arial', 18)
display_font=('Arial',32)

#Initialize the Quantum Circuit
def initialize_circuit():
    global circuit
    circuit=QuantumCircuit(1)

initialize_circuit()
theta=0

def display_gate(gate_input):
    #adds corresponding gate notation in the display to track operation
    #disable buttons if the number of operations reach 10

    display.insert(tkinter.END,gate_input)
    input_gates=display.get()
    num_gates_pressed=len(input_gates)
    list_input_gates=list(input_gates)
    search_word=["R","D"]
    count_double_valued_gates=[list_input_gates.count(i) for i in search_word]
    num_gates_pressed-=sum(count_double_valued_gates)
    if num_gates_pressed==10:
        gates=[x_gate,y_gate,z_gate,Rx_gate,Ry_gate,Rz_gate,s_gate,sd_gate,t_gate,td_gate,hadamard_gate]
        for gate in gates:
            gate.config(state=tkinter.DISABLED)

def clear(circuit):
    """
    clears the display and Reintializes the Quantum circuit doe fresh calculation
    Checks if the gate buttons are disabled, if so enables the buttons
    """

    #clear the display
    display.delete(0,tkinter.END)
    #reset the circuit to intial conditons
    initialize_circuit()

    #Checks if the buttons are disabled and if so,enables them
    if x_gate['state']==tkinter.DISABLED:
        gates=[x_gate,y_gate,z_gate,Rx_gate,Ry_gate,Rz_gate,s_gate,sd_gate,t_gate,td_gate,hadamard_gate]
        for gate in gates:
            gate.config(state=tkinter.NORMAL)
    





def about():
    #display information about the project

    info=tkinter.Tk()
    info.title('About')
    info.geometry('720x500')
    info.resizable(0,0)

    text=tkinter.Text(info,height=20,width=20)
    label=tkinter.Label(info,text="About Visualising Quantum Gate")


    Text_to_Display="""
    This is a Visualization tool for Single Qubit rotation on the Block sphere

    Quantum Gate buttons used in this app along with thier corresponding qiskit commands:

    X = Pauli-X gate flips the state of qubit -                        circuit.x()
    Y = Pauli-Y rotates the state vector about Y-axis -                circuit.y()
    Z = Pauli-Z flips the phase by PI radians -                        circuit.z()
    Rx = Parameterised rotation about the X axis -                     circuit.rx()
    Ry = Parameterised rotation about the Y axis -                     circuit.ry()
    Rz = Parameterised rotation about the Z axis -                     circuit.rz()
    S = rotates the state vector about the Z axis by PI/2 radians -    circuit.s()
    T = rotates the state vector about the Z axis by PI/4 radians -    circuit.t()
    Sd = rotates the state vector about the Z axis by -PI/2 radians -  circuit.sdg()
    Td = rotates the state vector about the Z axis by -PI/4 radians -  circuit.tdg()
    H = Creates a state of superposition -                             circuit.h()

    For Rx, Ry and Rz,Itheta(rotation_angle) allowed range in the app is [-2*PI,2*PI]

    Incase there is an visualization error the app closes automatically.
    This indicates that visualization of your circuit is not possible.        

    At a time, only ten operations can be visualized  
    """
    label.pack()
    text.pack(fill='both',expand=True)

    text.insert(tkinter.END,Text_to_Display)

    info.mainloop()

def visualize_circuit(circuit,window):
    """
    Visualizes the single qubit rotations corresponding to applied gates in a separate tkinter window.
    Handles any possible visualization error
    """
    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.VisualizationError:
        window.destroy()

def change_theta(num,window,circuit,key):
    """
    Changes the global variable theta and destroys the window
    """
    global theta
    theta =num*np.pi
    if key=='X':
        circuit.rx(theta,0)
        theta=0
    elif key=='Y':
        circuit.ry(theta,0)
        theta=0
    else:
        circuit.rz(theta,0)
        theta=0
    window.destroy()






def user_input(circuit,key):
    """
    Takes the user input for the rotation angle for parameterised
    Rotation gates Rx,ry,Rz.
    """
    get_input=tkinter.Tk();
    get_input.title("Get theta")
    get_input.geometry('360x160')
    get_input.resizable(0,0)
    
    val1=tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='PI/4',command=lambda:change_theta(0.25,get_input,circuit,key))
    val2=tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='PI/2',command=lambda:change_theta(0.50,get_input,circuit,key))
    val3=tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='PI',command=lambda:change_theta(1.0,get_input,circuit,key))
    val4=tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='2*PI',command=lambda:change_theta(2.0,get_input,circuit,key))
    val5=tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='-PI/4',command=lambda:change_theta(-0.25,get_input,circuit,key))
    val6=tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='-PI/2',command=lambda:change_theta(-0.50,get_input,circuit,key))
    val7=tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='-PI',command=lambda:change_theta(-1.0,get_input,circuit,key))
    val8=tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial",10),text='-2*PI',command=lambda:change_theta(-2.0,get_input,circuit,key))
    val1.grid(row=0,column=0)
    val2.grid(row=0,column=1)
    val3.grid(row=0,column=2)
    val4.grid(row=0,column=3,sticky='W')
    val5.grid(row=1,column=0)
    val6.grid(row=1,column=1)
    val7.grid(row=1,column=2)
    val8.grid(row=1,column=3,sticky='W')

    text_object=tkinter.Text(get_input,height=20,width=20,bg="light cyan")
    note="""
    Give the value for theta
    The value has the range [-2*PI,2*PI]
    """

    text_object.grid(sticky='WE',columnspan=4)
    text_object.insert(tkinter.END,note)




display_frame=tkinter.LabelFrame(root)
button_frame=tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both',expand=True)

display=tkinter.Entry(display_frame,width=120,font=display_font
,bg=background,borderwidth=5,justify=tkinter.LEFT)
display.pack(padx=1,pady=2)



#define the first row of buttons
x_gate=tkinter.Button(button_frame, font=button_font, bg=buttons,text='X',command=lambda:[display_gate('X'),circuit.x(0)])
y_gate=tkinter.Button(button_frame, font=button_font, bg=buttons,text='Y',command=lambda:[display_gate('Y'),circuit.y(0)])
z_gate=tkinter.Button(button_frame, font=button_font, bg=buttons,text='Z',command=lambda:[display_gate('Z'),circuit.z(0)])
x_gate.grid(row=0,column=0,ipadx=45, pady=1)
y_gate.grid(row=0,column=1,ipadx=45, pady=1)
z_gate.grid(row=0,column=2,ipadx=53, pady=1,sticky='E')

#Second Row
Rx_gate=tkinter.Button(button_frame,font=button_font,bg=buttons,justify=tkinter.CENTER,text='RX',command=lambda:[display_gate('Rx'),user_input(circuit,'x')])
Ry_gate=tkinter.Button(button_frame,font=button_font,bg=buttons,text='RY',command=lambda:[display_gate('Ry'),user_input(circuit,'y')])
Rz_gate=tkinter.Button(button_frame,font=button_font,bg=buttons,text='RZ',command=lambda:[display_gate('Rz'),user_input(circuit,'z')])
Rx_gate.grid(row=1,column=0,columnspan=1,sticky='WE', pady=1)
Ry_gate.grid(row=1,column=1,columnspan=1,sticky='WE', pady=1)
Rz_gate.grid(row=1,column=2,columnspan=1,sticky='WE', pady=1)

#Third Row
s_gate=tkinter.Button(button_frame,font=button_font,bg=buttons,text='S',command=lambda:[display_gate('S'),circuit.s(0)])
sd_gate=tkinter.Button(button_frame,font=button_font,bg=buttons,text='SD',command=lambda:[display_gate('SD'),circuit.sdg(0)])
hadamard_gate=tkinter.Button(button_frame,font=button_font,bg=buttons,text='H',command=lambda:[display_gate('H'),circuit.h(0)])
s_gate.grid(row=2,column=0,columnspan=1,sticky='WE', pady=1)
sd_gate.grid(row=2,column=1,columnspan=1,sticky='WE', pady=1)
hadamard_gate.grid(row=2,column=2,rowspan=2,sticky='WENS', pady=1)

#Fourth Row
t_gate=tkinter.Button(button_frame,font=button_font,bg=buttons,text='T',command=lambda:[display_gate('T'),circuit.t(0)])
td_gate=tkinter.Button(button_frame,font=button_font,bg=buttons,text='TD',command=lambda:[display_gate('TD'),circuit.tdg(0)])
t_gate.grid(row=3,column=0,columnspan=1,sticky='WE', pady=1)
td_gate.grid(row=3,column=1,columnspan=1,sticky='WE', pady=1)

# Define Quit and Visualize methods
quit=tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Quit',command=root.destroy)
visualize=tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Visualize',command=lambda:visualize_circuit(circuit,root))
quit.grid(row=4,column=0,columnspan=2,sticky='WE',ipadx=5, pady=1)
visualize.grid(row=4,column=2,columnspan=1,sticky='WE',ipadx=8, pady=1)


# Define the clear button
clear_button=tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Clear',command=lambda:clear(circuit))
clear_button.grid(row=5,column=0,columnspan=3,sticky='WE')

# Define the About button
about_button=tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='About',command=about)
about_button.grid(row=6,column=0,columnspan=3,sticky='WE')




#Run main loop
root.mainloop()
