import copy

def apply_event(state, event):
	new_state = copy.deepcopy(state)
	if event.event_type == "process_start"
		pid = event.details["pid"]
		new_state.processes[pid] = event.details
	elif event.event_type == "file_access":
		path = event.details["path"]
		new_state.files[path] = event.details
	return new_state 
