import { Html, Head, Body, Text } from '@react-email/components';

const TestEMail = () => (
  <Html>
    <Head />
    <Body>
      <Text>Hello,</Text>
      <Text>This is a test email sent from our React application!</Text>
      <Text>Best regards,</Text>
      <Text>Your Company</Text>
    </Body>
  </Html>
);

export default TestEMail;