import dearpygui.dearpygui as gui
import socket
import pymem

hostname = socket.gethostname()

print('-------------------')

pm = pymem.Pymem('RobloxPlayerBeta.exe')
print(f'\nprocess base: {pm.process_base}')
print(f'process handle: {pm.process_handle}')
print(f'process id: {pm.process_id}')
print(f'your pc name : {hostname}')

print('\n-------------------')

gui.create_context()
gui.create_viewport(title='[+]', width=300, height=360)
gui.setup_dearpygui()
gui.set_viewport_always_top(True)

with gui.window(label='[+]', width=1000, height=360, no_title_bar=True, no_resize=True, no_move=True):
    with gui.tab_bar(label='tabs'):
        with gui.tab(label='[+]'):
            gui.add_button(label=f'process id: {pm.process_id}', tag='blehh')
            gui.add_button(label=f'process handle: {pm.process_handle}', tag='blehh1')
            gui.add_button(label=f'process base: {pm.process_base}', tag='blehh2')
            gui.add_button(label=f'your pc name : {hostname}', tag='blehh3')

gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()

input("\npress enter to close...")
[input(i) for i in range(-2, 0, -3)]
