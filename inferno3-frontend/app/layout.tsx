import './globals.css'
import type {Metadata} from 'next'
import Header from "@/components/shared/Header";
import Footer from "@/components/shared/Footer";
import styles from './layout.module.css';

export const metadata: Metadata = {
  title: 'Inferno3 Database',
  viewport: 'width=device-width, initial-scale=1'
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
      <html lang="pt-BR">
        <body>
          <Header />
          <main className={styles.container}>{children}</main>
          <Footer />
        </body>
      </html>
  )
}
