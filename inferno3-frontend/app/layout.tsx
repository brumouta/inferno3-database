import './globals.css'
import type {Metadata} from 'next'
import {Inter} from 'next/font/google'
import TopNavbar from './components/TopNavbar'
import Sidebar from '@/components/Sidebar'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Inferno3 Database',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
      <section>
        <TopNavbar/>
      </section>
      <div>
        <Sidebar/>
      </div>
      {children}
      </body>
    </html>
  )
}
