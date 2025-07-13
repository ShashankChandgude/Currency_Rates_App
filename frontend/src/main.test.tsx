import { describe, it, expect } from 'vitest'
import React from 'react'
import ReactDOM from 'react-dom/client'

describe('main.tsx', () => {
  it('can import React', () => {
    expect(React).toBeDefined()
  })

  it('can import ReactDOM', () => {
    expect(ReactDOM).toBeDefined()
    expect(ReactDOM.createRoot).toBeDefined()
  })

  it('can import App component', async () => {
    const { default: App } = await import('./App')
    expect(App).toBeDefined()
  })
}) 