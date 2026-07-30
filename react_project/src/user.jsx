import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(5);

  return (
    <>
      <button onClick={() => setCount(count > 0 ? count - 1 : 0)}>-</button>
      <h1>{count}</h1>
      <button onClick={() => setCount(count + 1)}>+</button>

      <input type="text" />
      <p></p>
      

    </>
  );
}

export default Counter;