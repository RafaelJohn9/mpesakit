import React from 'react';
import Layout from '@theme/Layout';
import { MpesaKitLanding } from '../components/MpesaKitLanding';

export default function Home(): React.ReactElement {
  return (
    <Layout title="MpesaKit" description="Python M-Pesa SDK">
      <MpesaKitLanding />
    </Layout>
  );
}