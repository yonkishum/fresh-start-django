import {Link} from 'react-router-dom'

export function Navigation() {
    return (
        <div>
            <Link to="/tasks">Task App</Link>

            <h1>Tasks App</h1>
            <Link to="/tasks-create">Create Tasks</Link>
        </div>
    );
}