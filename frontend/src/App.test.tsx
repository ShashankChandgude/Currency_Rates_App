import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import App from './App'

describe('App', () => {
  it('renders the main heading', () => {
    render(<App />)
    expect(screen.getByText('Currency Converter & Charting App')).toBeInTheDocument()
  })

  it('renders the description text', () => {
    render(<App />)
    expect(screen.getByText(/Real-time currency conversion with live exchange rates and historical charts/)).toBeInTheDocument()
  })

  it('renders the frontend ready message', () => {
    render(<App />)
    expect(screen.getByText(/Frontend is ready! Backend integration coming soon/)).toBeInTheDocument()
  })

  it('has the correct CSS classes', () => {
    render(<App />)
    const mainDiv = screen.getByText('Currency Converter & Charting App').closest('div')
    expect(mainDiv).toHaveClass('container', 'mx-auto', 'px-4', 'py-8')
  })
}) 