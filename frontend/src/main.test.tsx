import { describe, it, expect } from 'vitest'

describe('main.tsx', () => {
  it('can import React', () => {
    const React = require('react')
    expect(React).toBeDefined()
  })

  it('can import ReactDOM', () => {
    const ReactDOM = require('react-dom/client')
    expect(ReactDOM).toBeDefined()
    expect(ReactDOM.createRoot).toBeDefined()
  })

  it('can import App component', async () => {
    const { default: App } = await import('./App')
    expect(App).toBeDefined()
  })
}) 