import { useState } from 'react'

export default function About() {
    const [localData] = useState({ ...localStorage })

    return (
        <>
            <div>About myself lorem ipsum </div>
            <div>{JSON.stringify(localData)}</div>
        </>
    )
}
